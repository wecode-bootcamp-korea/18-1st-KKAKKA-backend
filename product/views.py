import json

from django.http      import JsonResponse, HttpResponse
from django.views     import View

from .models        import *


class ProductView(View):
    def get(self, request):
        products  = Product.objects.all()
        # sizes     = ProductSize.objects.all()
        

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
                    'created_at'       : product.created_at
                }
            )
            # if Product.name == ProductSize.product.name: #product_id인지 shell에서 확인
            #     results[0]['size'] = ProductSize.size
            images    = ProductImage.objects.filter(product=product.id)
            print('88888888888')#이미지 for 돌려서 
            print(images[0].url)

            if product.id == images[0].id:
                results[0]['images'] = ProductImage.url

        return JsonResponse({'result':results}, status=200)


class ProductDetailView(View):
    def get(self, request):
        products  = Product.objects.all()
        # sizes     = ProductSize.objects.all()
        images    = ProductImage.objects.get(Product.name)
        option    = option.objects.all()

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
            if Product.name == ProductSize.product.name: #product_id인지 shell에서 확인
                results[0]['size'] = ProductSize.size

            if Product.name == ProductImage.product.name:
                results[0]['images'] = {
                    ProductImage.url,
                    ProductImage.url,
                    ProductImage.url,

                }
                
        return JsonResponse({'result':results}, status=200)