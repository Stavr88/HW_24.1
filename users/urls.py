from django.urls import path


from users.apps import UsersConfig
from rest_framework.routers import SimpleRouter

from users.views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

router = SimpleRouter()
router.register('', PaymentViewSet, basename='payment')

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('view/', UserListAPIView.as_view(), name='list_view'),
    path('view/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_detail'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_change'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user_delete'),
    path('token/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
]

urlpatterns += router.urls

