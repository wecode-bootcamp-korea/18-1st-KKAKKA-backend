import json
from json import JSONDecodeError

from django.http            import JsonResponse, HttpResponse
from django.utils.dateparse import parse_date
from django.views           import View

from .models              import Order, Status, SubscriptionCart
from subscription.models  import Subscription, SubscriptionPlan

#subscription 주문
class SubscriptionOrderView(View):
    # @Validator
    # @transaction 쓰기
    def post(self, request, subscription_id):
        try:
            data = json.loads(request.body)
            
            account           = data['account']
            monthly_plan      = data['monthly_plan'] #정기결제->plan # string으로 들어온단밀이지? id값으로 보내주는 지 확인
            quantity          = data['quantity']
            delivery_date     = data['dlivery_date'] #"2021-03-26"

            #order 생성, status default = '결제 전'
            order = Order.objects.create(account_id = account, status_id = Order.status.get(id=1))

            #subsriptionCart
            temp_date = parse_date(delivery_date)

            SubscriptionCart.objects.create(
                order         = order.id,
                subscription  = SubscriptionPlan.filter(subscription = subscription_id, monthly_plan = monthly_plan),
                quantity      = int(quantity),
                delivery_date = temp_date
            )

            return JsonResponse({'message':'SUCCESS'}, status=200)

        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except Subscription.DoesNotExist:
            return JsonResponse({'message': 'Subscription_DOES_NOT_EXIST'}, status=404)
        except SubscriptionPlan.DoesNotExist:
            return JsonResponse({'message': 'SubscriptionPlan_DOES_NOT_EXIST'}, status=404)
            
