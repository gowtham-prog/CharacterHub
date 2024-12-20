# TODO There's certainly more than one way to do this task, so take your pick.

import django.contrib.auth.models
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email'] 

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        comments = instance.comments.order_by('timestamp')

        # TO fetch 3 commments randonly
        # comments = instance.comments.order_by('?')[:3]
        
        data['comments'] = CommentSerializer(comments, many=True).data
        return data


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
    
