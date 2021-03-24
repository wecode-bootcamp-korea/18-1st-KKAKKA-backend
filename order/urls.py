<<<<<<< HEAD

from django.urls import path

from .views      import SubscriptionOrderView

urlpatterns = [
    path('/subscription/<int:subscription_id>', SubscriptionOrderView.as_view()),
]
=======
from django.urls import path, include
from account.views     import ProductCartView


urlpatterns = [
    path('/product_cart', ProductCartView.as_view()),
    ] 
>>>>>>> main
