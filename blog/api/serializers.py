from rest_framework import serializers
from blog.models import Post, Comment
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'author', 'body', 'status', 'created']


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title']


class CommentSerializer(serializers.ModelSerializer):
    post = PostCommentSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['post', 'id', 'name', 'email', 'body', 'created', 'active']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'email', 'groups')
