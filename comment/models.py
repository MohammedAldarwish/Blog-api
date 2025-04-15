from django.db import models
from django.conf import settings

class Comment(models.Model):
    blog = models.ForeignKey('api.BlogModel', on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"comment by {self.author} on {self.blog}"