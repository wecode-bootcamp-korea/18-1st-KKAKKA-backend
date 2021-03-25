import json
from json import JSONDecodeError

from django.http            import JsonResponse, HttpResponse
from django.utils.dateparse import parse_date
from django.views           import View

from .models              import Order, Status, SubscriptionCart
from subscription.models  import Subscription, SubscriptionPlan
from account.models       import Account
from product.models       import OptionSubscription

#subscription 주문
class SubscriptionOrderView(View):
    # @Validator
    # @transaction 쓰기
    def post(self, request, subscription_id):
        try:
            data = json.loads(request.body)

            account           = data['account']          
            monthly_plan      = data['monthly_plan']
            quantity          = data['quantity']
            delivery_date     = data['delivery_date']
            option            = data['option']

            temp_date         = parse_date(delivery_date)
            status            = Status.objects.get(id = 1)
            account           = Account.objects.get(id = account)
            option            = OptionSubscription.objects.get(id = option)
            subscriptionplans = SubscriptionPlan.objects.get(subscription_id = subscription_id, monthly_plan_id = monthly_plan)

            order = Order.objects.create(account_id = account.id, status_id = status.id)

            if order:
                SubscriptionCart.objects.create(
                    order_id               = order.id,
                    subscription_id        = subscriptionplans.id,
                    subscription_option_id = option.id,
                    quantity               = quantity,
                    delivery_date          = temp_date
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
            
