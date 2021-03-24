from django.urls import path

from .views             import MainView
from subscription.views import SubscriptionView
from .views      import ProductView, ProductDetailView

urlpatterns = [
    path('', ProductView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
    path('/main', MainView.as_view()),
    path('', SubscriptionView.as_view()),
]

