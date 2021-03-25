import json
from json import JSONDecodeError

from django.http            import JsonResponse, HttpResponse
from django.utils.dateparse import parse_date
from django.views           import View

from .models              import Order, Status, SubscriptionCart, Address
from subscription.models  import Subscription, SubscriptionPlan
from account.models       import Account
from product.models       import OptionSubscription


class SubscriptionOrderView(View):
    # @Validator
    # @transaction
    def post(self, request, subscription_id):
        try:
            data = json.loads(request.body)

            account_id           = data['account']          
            monthly_plan_id      = data['monthly_plan']
            quantity             = data['quantity']
            delivery_date        = data['delivery_date']
            option_id            = data['option']

            temp_date         = parse_date(delivery_date)
            status            = Status.objects.get(id = 1)
            account           = Account.objects.get(id = account_id)
            option            = OptionSubscription.objects.get(id = option_id)
            subscriptionplans = SubscriptionPlan.objects.get(subscription_id = subscription_id, monthly_plan_id = monthly_plan_id)

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
            

class AddressView(View):
    def post(self, request):
        try:    
            data            = json.loads(request.body)
            recipient_phone = data['recipient_phone']
            postal_code     = data['postal_code']
            recipient       = data['recipient']
            address         = data['address']
            sender          = data['sender']
            save_option     = data['save']

            Address.objects.create(sender=sender, recipient=recipient,recipient_phone_number=recipient_phone, postal_code=postal_code, address=address, save_option=save_option)
            return JsonResponse({'message':'success_address_input'}, status = 201)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)            

        except JSONDecodeError:
            return JsonResponse({'message': 'JSONDecodeError'}, status=400)