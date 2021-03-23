import json
from json import JSONDecodeError

from django.http      import JsonResponse, HttpResponse
from django.views     import View

from .models              import *
from subscription.models  import *

#subscription 주문
class SubscriptionView(View):
    #@Validator
    def post(self, request, subscription_id):
        try:
            data = json.loads(request.body)
            
            user              = data['user']
            subscription_id   = data['id']
            quantity          = data['quantity']
            delivery_date     = data['dlivery_date']
            option            = data['option']



            results = []

            results.append(
                {
                    'id'               : subscription.id,
                    'name'             : subscription.name,
                    'detail'           : subscription.introduction,
                    'orign_price'      : subscription.orign_price,
                    'discount_rate'    : subscription.discount_rate,
                    'discounted_price' : subscription.discounted_price,
                    'created_at'       : subscription.created_at,
                    'image'            : subscription.main_image,
                    'size'             : subscription.size.name
                }
            )
            return JsonResponse({'result':results}, status=200)

        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except Product.DoesNotExist:
            return JsonResponse({'message': 'Product_DOES_NOT_EXIST'}, status=404)