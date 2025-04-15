from rest_framework import viewsets
from .models import BlogModel
from .serializers import BlogSerializers
from .permissions import IsAuthorOrReadOnly
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend
from .filters import BlogFilter
class BlogView(viewsets.ModelViewSet):


    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializers
    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BlogFilter

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user)
        else:
            raise PermissionDenied("You must be logged in to create a blog post.")
    
    
    