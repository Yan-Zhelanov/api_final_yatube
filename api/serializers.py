from rest_framework.serializers import (CharField, ModelSerializer,
                                        SlugRelatedField, ValidationError)
from rest_framework.validators import UniqueTogetherValidator

from .models import Comment, Follow, Group, Post, User


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    group = CharField(source='group.title', required=False)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True)
    following = SlugRelatedField(slug_field='username',
                                 queryset=User.objects.all())

    def validate(self, attrs):
        if self.context['request'].user == attrs['following']:
            raise ValidationError('Нельзя подписаться на самого себя.')
        return attrs

    class Meta:
        model = Follow
        fields = ('user', 'following',)
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['following'],
                message='Вы уже подписаны на этого пользователя.')
        ]
