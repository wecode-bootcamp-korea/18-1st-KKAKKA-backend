from django.urls import path

from .views             import MainView
from subscription.views import SubscriptionView

urlpatterns = [
    path('/main', MainView.as_view()),
    path('', SubscriptionView.as_view())
]