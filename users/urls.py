from django.urls import path
from rest_framework.permissions import AllowAny

from users.apps import UsersConfig
from rest_framework.routers import SimpleRouter

from users.views import PaymentViewSet


app_name = UsersConfig.name

router = SimpleRouter()
router.register('', PaymentViewSet, basename='payment')

urlpatterns = [

]

urlpatterns += router.urls
