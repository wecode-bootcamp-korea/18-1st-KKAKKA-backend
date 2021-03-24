import json
from json import JSONDecodeError

from django.http      import JsonResponse, HttpResponse
from django.views     import View

from .models              import Order, Status, SubscriptionCart
from subscription.models  import Subscription

#subscription 주문
class SubscriptionOrderView(View):
    # @Validator
    # @transaction 쓰기
    def post(self, request, subscription_id):
        try:
            data = json.loads(request.body)
            
            account           = data['account']
            subscription_id   = data['id']
            monthly_plan      = data['monthly_plan']
            quantity          = data['quantity']
            delivery_date     = data['dlivery_date']

            #order 생성, status default = '결제 전'
            Order.objects.create(account = account, status = Order.status.get(id=1))

            #subsriptionCart
            SubscriptionCart.objects.create(
                order         = [
                    {account.id} 
                    for order in SubscriptionCart.order.filter(account=account, created_at = 생성일 최신)
                ]
                subscription  = subscription_id
                quantity      = quantity
                delivery_date = delivery_date
            )

            return JsonResponse({'result':results}, status=200)

        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except Product.DoesNotExist:
            return JsonResponse({'message': 'Product_DOES_NOT_EXIST'}, status=404)