import json
from json import JSONDecodeError

from django.http      import JsonResponse, HttpResponse
from django.views     import View

from product.models        import Product


class MainProductView(View):
    def get(self, request):
        try:
            products       = Product.objects.all()

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

            return JsonResponse({'product_list':product_list[0:8]}, status=200)
        
        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except Product.DoesNotExist:
            return JsonResponse({'message': 'Product_DOES_NOT_EXIST'}, status=404)



class ProductView(View):
    def get(self, request):
        try:
            products  = Product.objects.all()

            results = [
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
                for product in products
            ]

            return JsonResponse({'result':results}, status=200)

        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except Product.DoesNotExist:
            return JsonResponse({'message': 'Product_DOES_NOT_EXIST'}, status=404)


class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product  = Product.objects.get(id=product_id)
            
            results = [
                {
                    'id'               : product.id,
                    'name'             : product.name,
                    'introduction'     : product.introduction,
                    'orign_price'      : product.orign_price,
                    'discount_rate'    : product.discount_rate,
                    'discounted_price' : product.discounted_price,
                    'size'             : product.size.name,
                    'images'           : [
                        image.url 
                        for image in product.productimage_set.filter(product=product_id)
                        ]
                }
            ]

            return JsonResponse({'result':results}, status=200)

        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except Product.DoesNotExist:
            return JsonResponse({'message': 'Product_DOES_NOT_EXIST'}, status=404)