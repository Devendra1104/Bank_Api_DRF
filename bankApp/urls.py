from django.urls import path
from .views import BankListView

urlpatterns = [
    path('bank/',BankListView.as_view(),name = 'banks'),
]