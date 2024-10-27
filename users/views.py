from rest_framework import filters
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from users.models import Payments, User
from users.permission import IsModerator, IsOwner
from users.serializers import PaymentsSerializer, UserSerializer


class PaymentViewSet(ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ('payment_time', 'price',)
    search_fields = ('payment_method',)
    filterset_fields = ('payment_time', 'payment_course', 'payment_lesson', 'payment_method',)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]


class UserDeleteAPIView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


