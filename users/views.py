from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from users.models import Payments
from users.serializers import PaymentsSerializer


class PaymentViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ('payment_time', 'price',)
    search_fields = ('payment_method',)
    filterset_fields = ('payment_time', 'payment_course', 'payment_lesson', 'payment_method',)
