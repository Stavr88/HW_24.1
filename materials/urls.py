from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import *

app_name = MaterialsConfig.name

router = SimpleRouter()

router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListApiView.as_view(), name="lesson_list"),
    path("lessons/create/", LessonCreateApiView.as_view(), name="lesson_create"),
    path("lessons/<int:pk>/update/", LessonUpdateApiView.as_view(), name="lesson_update"),
    path("lessons/<int:pk>/delete/", LessonDestroyApiView.as_view(), name="lesson_delete"),
    path("lessons/<int:pk>/", LessonRetrieveApiView.as_view(), name="lesson_retrieve"),
    path('subscription/', SubscriptionCreateApiView.as_view(), name='subscription'),
]

urlpatterns += router.urls

