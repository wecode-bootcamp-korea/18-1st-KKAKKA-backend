from django.urls import path

from .views      import SubscriptionView, SubscriptionDetailView

urlpatterns = [
    path('', SubscriptionView.as_view()),
    path('/<int:subscription_id>', SubscriptionDetailView.as_view())
]