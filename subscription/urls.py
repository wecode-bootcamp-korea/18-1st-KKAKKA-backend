from django.urls import path

from .views      import SubscriptionView, ProductDetailView

urlpatterns = [
    #상품 전체 페이지
    path('/', SubscriptionView.as_view()),
    #상품 상세페이지
    path('/contents/<int:subscription_id>', ProductDetailView.as_view())
]