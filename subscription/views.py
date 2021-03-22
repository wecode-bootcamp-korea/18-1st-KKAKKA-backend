import json
from json import JSONDecodeError

from django.http      import JsonResponse, HttpResponse
from django.views     import View

from .models        import *

#전체구독상품 페이지
# 가격 manytomany 역참조 확인해서 입력하기
class SubscriptionView(View):
    def get(self, request):
        try:
            subscriptions  = Subscription.objects.all()
            prices          = SubscriptionPlan.objects.all()

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
                # price = []
                
                # for price in prices:
                #     print(price)
                #     p1 = price.objects.filter(monthly_id)
                #     print('******')
                #     print(p1)
                #     print('********')
                    # price.appned(
                    #     {
                    #         filter(monthly_plan.name == '정기결제')

                    #     }
                    # )
            return JsonResponse({'result':results}, status=200)

        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except Subscription.DoesNotExist:
            return JsonResponse({'message': 'Product_DOES_NOT_EXIST'}, status=404)



#상품 상세페이지
# 가격 manytomany 역참조 확인해서 입력하기
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
                    # 'price'            : subscription.orign_price,
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