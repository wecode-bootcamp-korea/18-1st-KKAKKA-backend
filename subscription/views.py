import json
from json import JSONDecodeError

from django.http      import JsonResponse, HttpResponse
from django.views     import View

from .models         import *
from product.models  import Category


#정기구독 전체보기 페이지
class SubscriptionView(View):
    def get(self, request):
        try:
            subscriptions = Subscription.objects.all()

            results = []
            
            for subscription in subscriptions:
                results.append(
                    {
                        'id'               : subscription.id,
                        'name'             : subscription.name,
                        'detail'           : subscription.introduction,
                        'price'            : subscription.orign_price,
                        'image'            : subscription.main_image,
                    }
                )
            return JsonResponse({'result':results}, status=200)

        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except Subscription.DoesNotExist:
            return JsonResponse({'message': 'Product_DOES_NOT_EXIST'}, status=404)
