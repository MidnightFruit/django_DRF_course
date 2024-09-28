from rest_framework.pagination import PageNumberPagination


class CoursesPaginator(PageNumberPagination):
    max_page_size = 10
    page_size = 10
    page_size_query_param = 'page_size'


class LessonsPaginator(PageNumberPagination):
    max_page_size = 10
    page_size = 10
    page_size_query_param = 'page_size'
