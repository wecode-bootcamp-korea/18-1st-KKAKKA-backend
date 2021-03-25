from django.urls import path
from .views      import AddressView,ReceiverView


urlpatterns = [
    path('/address', AddressView.as_view()),
    path('/receiver', ReceiverView.ad_view())
    ] 