from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import Comment, Follow, Group, Post, User


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    group = SlugRelatedField(slug_field='title', queryset=Group.objects.all(),
                             required=False)

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'pub_date', 'group')


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ('title',)


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True)
    following = SlugRelatedField(slug_field='username',
                                 queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = ('user', 'following',)
