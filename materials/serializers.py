from rest_framework import serializers

from materials.models import Course, Lesson, Subscribe
from materials.validators import YouTubeURLValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('name', 'description', 'preview', 'video_url', 'course')
        validators = [YouTubeURLValidator(field='video_url')]


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        field = 'course'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(read_only=True, many=True)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    subscriptions = serializers.SerializerMethodField()

    def get_lessons_count(self, obj):
        return Lesson.objects.filter(course=obj).count()

    def get_subscriptions(self, course):
        subscription = Subscribe.objects.filter(course=course)
        subed_emails = []
        for sub in subscription:
            subed_emails.append(sub.user.email)
        return subed_emails


    class Meta:
        model = Course
        fields = ('pk' ,'name', 'preview', 'description', 'lessons_count', 'lessons', 'owner', 'subscriptions')


