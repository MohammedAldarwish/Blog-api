from rest_framework import permissions
from rest_framework.generics import ListAPIView
from .models import Comment
from .serializers import CommentSerializers


class CommentListView(ListAPIView):
    serializer_class = CommentSerializers
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        blog_id = self.kwargs['blog_id']
        return Comment.objects.filter(blog_id=blog_id)    

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    