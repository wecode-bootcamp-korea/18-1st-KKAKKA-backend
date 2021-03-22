
from django.urls import path

from .views      import ProductView, ProductDetailView

urlpatterns = [
    #상품 전체 페이지
    path('/products', ProductView.as_view()),
    #상품 상세페이지
    path('/contents/<int:product_id>', ProductDetailView.as_view())
]