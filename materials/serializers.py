from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson, Subscription
from materials.validators import ValidatorLink


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [ValidatorLink(field='video_url')]


class CourseSerializer(ModelSerializer):
    lesson_count = SerializerMethodField()
    lessons_info = SerializerMethodField()

    def get_lesson_count(self, object):
        return object.lesson_set.count()

    def get_lessons_info(self, object):
        return LessonSerializer(object.lesson_set.all(), many=True).data

    class Meta:
        model = Course
        fields = ("name", "description", "image", "lesson_count", "lessons_info")


class CourseDetailSerializer(ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')
    subscription = SerializerMethodField()

    def get_subscription(self, course):
        user = self.context['request'].user
        return Subscription.objects.all().filter(user=user).filter(course=course).exists()

    class Meta:
        model = Course
        fields = ('lessons', 'subscription')


class SubscriptionSerializer(ModelSerializer):
    class Meta:
        model = Subscription
        fields = ("status_of_subscription",)



