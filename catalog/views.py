from rest_framework.viewsets import ReadOnlyModelViewSet
from catalog.models import Product
from catalog.serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination
from .filters import ProductFilter


class ProductPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        response.data['total'] = self.page.paginator.count
        response.data['pages'] = self.page.paginator.num_pages
        return response


class ProductView(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    filterset_class = ProductFilter
