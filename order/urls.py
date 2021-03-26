from django.urls import path

from .views      import SubscriptionOrderView, AddressView

urlpatterns = [
    path('/subscription/<int:subscription_id>', SubscriptionOrderView.as_view()),
    path('/address', AddressView.as_view())
]
