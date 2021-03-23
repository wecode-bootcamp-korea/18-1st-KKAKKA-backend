from django.urls import path

from .views      import MainView

urlpatterns = [
    #메인페이지
    path('/all', MainView.as_view()),
]