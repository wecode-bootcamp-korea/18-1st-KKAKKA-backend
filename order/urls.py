
from django.urls import path

from .views      import 

urlpatterns = [
    #상품 전체 페이지
    path('/subscription/<int:subscription_id>', .as_view()),
]