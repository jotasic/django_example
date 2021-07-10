from rest_framework import pagination

class BigPagePagination(pagination.PageNumberPagination):
    page_size = 30
