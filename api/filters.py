import django_filters
from .models import BlogModel

class BlogFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains')

    class Meta:
        model = BlogModel
        fields = ['author']
