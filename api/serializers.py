from rest_framework.serializers import (CharField, ModelSerializer,
                                        SlugRelatedField, ValidationError)

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
        fields = ('title',)


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True)
    following = SlugRelatedField(slug_field='username',
                                 queryset=User.objects.all())

    def validate(self, attrs):
        if (self.context['request'].user == attrs['following']
           or Follow.objects.filter(user=self.context['request'].user,
                                    following=attrs['following']).exists()):
            raise ValidationError(
                'Введено некорректное имя пользователя, либо вы уже '
                'подписаны на этого пользователя!'
            )
        return attrs

    class Meta:
        model = Follow
        fields = ('user', 'following',)
