import json
from json import JSONDecodeError

from django.http      import JsonResponse, HttpResponse
from django.views     import View

from .models        import *

#전체구독상품 페이지
class SubscriptionView(View):
    def get(self, request):
        try:
            subscriptions  = Subscription.objects.all()

            results = []

            for subscription in subscriptions:
                results.append(
                    {
                        'id'               : subscription.id,
                        'name'             : subscription.name,
                        'introduction'     : subscription.introduction,
                        'image'            : subscription.main_image,
                        'description'      : subscription.description,
                    }
                )
                
                prices = SubscriptionPlan.objects.get(subscription_id = subscription.id)
                results.append(
                    {
                        'price' : prices.price
                    }
                )

            return JsonResponse({'result':results}, status=200)

        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except Subscription.DoesNotExist:
            return JsonResponse({'message': 'Product_DOES_NOT_EXIST'}, status=404)



#상품 상세페이지
class ProductDetailView(View):
    def get(self, request, subscription_id):
        try:
            subscription  = Subscription.objects.get(id=subscription_id)
            results = []
            results.append(
                {
                    'id'               : subscription.id,
                    'name'             : subscription.name,
                    'introduction'     : subscription.introduction,
                    }
                )

            prices = SubscriptionPlan.objects.get(subscription_id = subscription.id)
            results.append(
                {
                    'price' : prices.price
                }
            )

            images = SubscriptionDetail.objects.filter(subscription=subscription_id)
            images_detail = []
            
            for image in images:
                images_detail.append(image.url)
                results[0]['images'] = images_detail

            return JsonResponse({'result':results}, status=200)

        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except Subscription.DoesNotExist:
            return JsonResponse({'message': 'Product_DOES_NOT_EXIST'}, status=404)