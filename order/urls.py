from django.urls import path, include
from account.views     import ProductCartView


urlpatterns = [
    path('/product_cart', ProductCartView.as_view()),
    ] 