from django.db import models
from accounts.models import CustomUser

class BlogModel(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=220, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.author