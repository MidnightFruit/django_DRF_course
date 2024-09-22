from rest_framework import viewsets
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from materials.models import Course, Lesson, Subscribe
from materials.paginators import LessonsPaginator, CoursesPaginator
from materials.serializers import CourseSerializer, LessonSerializer
from users.permissions import IsModerator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CoursesPaginator

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = (IsAuthenticated, ~IsModerator)
        elif self.action == 'list':
            self.permission_classes = (IsAuthenticated, IsOwner | IsModerator,)
        elif self.action == 'destroy':
            self.permission_classes = (IsOwner, ~IsModerator)
        elif self.action == 'update':
            self.permission_classes = (IsAuthenticated, IsOwner | IsModerator,)
        else:
            self.permission_classes = (IsOwner | IsModerator,)

        return [permission() for permission in self.permission_classes]


class LessonCreateAPIView(CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListAPIView(ListAPIView):
    pagination_class = LessonsPaginator
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class LessonRetrieveAPIView(RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner | IsModerator, IsAuthenticated]


class LessonUpdateAPIView(UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner | IsModerator, IsAuthenticated]


class LessonDestroyAPIView(DestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsOwner, IsAuthenticated]


class SubscribeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data['course']
        course_item = get_object_or_404(Course, pk=course_id)

        subs_item = Subscribe.objects.filter(user=user, course=course_item)

        # Если подписка у пользователя на этот курс есть - удаляем ее
        if subs_item.exists():
            subs_item.delete()
            message = 'подписка удалена'
        # Если подписки у пользователя на этот курс нет - создаем ее
        else:
            Subscribe.objects.create(user=user, course=course_item)
            message = 'подписка добавлена'
        # Возвращаем ответ в API
        return Response({"message": message})