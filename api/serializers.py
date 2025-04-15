from rest_framework import serializers 
from .models import BlogModel


class BlogSerializers(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = BlogModel
        fields = ['title','author' ,'created_at']

    def create(self, validated_data):
        validated_data['author'] == self.context['request'].user
        return super().create(validated_data)
    
    def get_author(self, obj):
        return obj.author.name
