from django.urls import path

from .views      import MainProductView, ProductView, ProductDetailView

urlpatterns = [
    path('', ProductView.as_view()),
    path('/<int:product_id>', ProductDetailView.as_view()),
    path('/main', MainProductView.as_view()),
]

