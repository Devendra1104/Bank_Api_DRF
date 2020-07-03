from django.shortcuts import render
from .serializers import BankSerializer
from .models import Bank
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class BankListView(generics.ListAPIView):
    serializer_class = BankSerializer
    queryset = Bank.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city', 'bank_name','ifsc']
