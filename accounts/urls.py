from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccountSignupAPIView.as_view(), name='signup'),
]
