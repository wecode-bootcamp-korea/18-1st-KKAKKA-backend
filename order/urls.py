
from django.urls import path

from .views      import SubscriptionOrderView

urlpatterns = [
    path('/cart/subscription/<int:subscription_id>', SubscriptionOrderView.as_view()),
]