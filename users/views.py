from django.shortcuts import render

from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework

from users.models import Payment
from users.serializers import PaymentSerializer


class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [SearchFilter, rest_framework.DjangoFilterBackend]
    ordering_fields = ['payment_date']
    filterset_fields  = ['method', 'course', 'lesson']
