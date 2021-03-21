import json
from json import JSONDecodeError

from django.http      import JsonResponse, HttpResponse
from django.views     import View

from .models        import *

#전체상품 페이지
class ProductView(View):
    def get(self, request):
        try:
            products  = Product.objects.all()

            results = []

            for product in products:
                results.append(
                    {
                        'id'               : product.id,
                        'name'             : product.name,
                        'detail'           : product.introduction,
                        'orign_price'      : product.orign_price,
                        'discount_rate'    : product.discount_rate,
                        'discounted_price' : product.discounted_price,
                        'created_at'       : product.created_at,
                        'image'            : product.main_image,
                        'size'             : product.size.name
                    }
                )
            return JsonResponse({'result':results}, status=200)

        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except Product.DoesNotExist:
            return JsonResponse({'message': 'Product_DOES_NOT_EXIST'}, status=404)



#상품 상세페이지
class ProductDetailView(View):
    def get(self, request):
        products  = Product.objects.all()
        results = []
        for product in products:
            results.append(
                {
                    'id'               : product.id,
                    'name'             : product.name,
                    'introduction'     : product.introduction,
                    'orign_price'      : product.orign_price,
                    'discount_rate'    : product.discount_rate,
                    'discounted_price' : product.discounted_price,
                }
            )

            images = ProductImage.objects.filter(product=product.id)
            images_detail = []
            for image in images:
                images_detail.append(image.url)
                print(images_detail)
                results[0]['images'] = images_detail

        return JsonResponse({'result':results}, status=200)