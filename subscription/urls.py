from django.urls import path

from .views      import SubscriptionView, ProductDetailView

urlpatterns = [
    path('/', SubscriptionView.as_view()),
    path('/<int:subscription_id>', ProductDetailView.as_view())
]