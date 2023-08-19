import rest_framework.serializers
from rest_framework.serializers import ModelSerializer
from blogs.models import Blog
from rest_framework.response import Response
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('__all__')