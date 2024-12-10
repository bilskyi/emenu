from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TestAPIView.as_view(),),
]