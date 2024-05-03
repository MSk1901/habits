from rest_framework.pagination import PageNumberPagination


class MyPagination(PageNumberPagination):
    """Пагинатор"""
    page_size = 5
    page_size_query_param = 'page_size'
