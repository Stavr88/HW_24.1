from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"


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



