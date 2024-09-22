from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials.views import CourseViewSet, LessonListAPIView, LessonCreateAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView, LessonRetrieveAPIView, SubscribeAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path("lessons/", LessonListAPIView.as_view(), name="lessons_list"),
    path("create_lessons/", LessonCreateAPIView.as_view(), name="create_lessons"),
    path('lesson/<int:pk>', LessonRetrieveAPIView.as_view(), name="retrieve_lessons"),
    path('delete_lesson/<int:pk>', LessonDestroyAPIView.as_view(), name="delete_lessons"),
    path('update_lesson/<int:pk>', LessonUpdateAPIView.as_view(), name="update_lessons"),
    path('subs/', SubscribeAPIView.as_view(), name='subs'),
] + router.urls
