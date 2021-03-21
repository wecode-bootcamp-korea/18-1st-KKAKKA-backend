import json

from django.http      import JsonResponse, HttpResponse
from django.views     import View

from .models        import *

#전체상품 페이지
class ProductView(View):
    def get(self, request):
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

#상품 상세페이지
class ProductDetailView(View):
    def get(self, request):
        products  = Product.objects.all()
        sizes     = ProductSize.objects.all()
        
        option    = option.objects.all()

        results = []

        for product in products:
            images = ProductImage.objects.filter(product=product.id)
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
            if Product.name == ProductSize.product.name: #product_id인지 shell에서 확인
                results[0]['size'] = ProductSize.size

            if Product.name == ProductImage.product.name:
                results[0]['images'] = {
                    ProductImage.url,
                    ProductImage.url,
                    ProductImage.url,

                }
                
        return JsonResponse({'result':results}, status=200)