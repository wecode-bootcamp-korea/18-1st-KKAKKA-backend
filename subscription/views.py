import json
from json import JSONDecodeError

from django.http      import JsonResponse, HttpResponse
from django.views     import View

from .models          import *

class SubscriptionView(View):
    def get(self, request):
        try:
            subscriptions  = SubscriptionPlan.objects.filter(monthly_plan_id=1)

            results = [ 
                {
                    'id'           : subscription.subscription.id, 
                    'name'         : subscription.subscription.name, 
                    'introduction' : subscription.subscription.introduction,
                    'image'        : subscription.subscription.main_image,
                    'description'  : subscription.subscription.description,
                    'price'        : subscription.price
                    
                } 
                for subscription in subscriptions
                if subscription
            ]

            return JsonResponse({'result':results}, status=200)

        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except Subscription.DoesNotExist:
            return JsonResponse({'message': 'Product_DOES_NOT_EXIST'}, status=404)



class ProductDetailView(View):
    def get(self, request, subscription_id):
        try:
            subscription  = Subscription.objects.get(id=subscription_id)
            prices        = subscription.subscriptionplan_set.get(subscription_id = subscription.id)
            images = subscription.subscriptiondetail_set.filter(subscription_id = subscription.id)
            images_detail = [ image.url for image in images ]

            results = []
            results.append(
                {
                    'id'               : subscription.id,
                    'name'             : subscription.name,
                    'introduction'     : subscription.introduction,
                    'price'            : prices.price,
                    'image'            : images_detail
                    }
                )

            return JsonResponse({'result':results}, status=200)

        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except Subscription.DoesNotExist:
            return JsonResponse({'message': 'Product_DOES_NOT_EXIST'}, status=404)