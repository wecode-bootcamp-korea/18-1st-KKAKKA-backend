import json
from json import JSONDecodeError

from django.http      import JsonResponse, HttpResponse
from django.views     import View

from product.models        import Product
from subscription.models   import Subscription


class MainView(View):
    def get(self, request):
        try:
            products       = Product.objects.all()
            subscriptions  = Subscription.objects.all()

            subscription_list = [
                {
                    'id'           : subscription.id,
                    'name'         : subscription.name,
                    'introduction' : subscription.introduction,
                    'image'        : subscription.main_image,
                    'price'        : subscription.subscriptionplan_set.get(subscription_id = subscription.id).price
                }
                for subscription in subscriptions
            ]

            product_list = [
                {
                    'id'               : product.id,
                    'name'             : product.name,
                    'introduction'     : product.introduction,
                    'image'            : product.main_image,
                    'orign_price'      : product.orign_price,
                    'discount_rate'    : product.discount_rate,
                    'discounted_price' : product.discounted_price,
                    'size'             : product.size.name,
                }
                for product in products
            ]

            return JsonResponse({'subscription_list':subscription_list, 'product_list':product_list[0:8]}, status=200)

        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except Subscription.DoesNotExist:
            return JsonResponse({'message': 'Product_DOES_NOT_EXIST'}, status=404)