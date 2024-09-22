from rest_framework import serializers

from materials.models import Course, Lesson, Subscribe
from materials.validators import YouTubeURLValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('name', 'description', 'preview', 'video_url', 'course')
        validators = [YouTubeURLValidator(field='video_url')]


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(read_only=True, many=True)
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def get_lessons_count(self, obj):
        return Lesson.objects.filter(course=obj).count()

    class Meta:
        model = Course
        fields = ('name', 'preview', 'description', 'lessons_count', 'lessons')


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        field = 'course'