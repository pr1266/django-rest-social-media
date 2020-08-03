from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from rest_framework import serializers
from .models import *

class UserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['username', 'phone_number', 'bio', 'image']

class UserCreateSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'

class FollowSerializer(ModelSerializer):

    follower = UserSerializer()
    followed = UserSerializer()

    class Meta:

        model = Follow
        fields = '__all__'

class FollowCreateSerializer(ModelSerializer):

    class Meta:

        model = Follow
        fields = '__all__'

class CommentReplySerializer(ModelSerializer):
    user = UserSerializer()
    comment = 'CommentSerializer'
    class Meta:
        depth = 1
        model = CommentReply
        fields = '__all__'
        

class CommentReplyCreateSerializer(ModelSerializer):

    class Meta:
        model = CommentReply 
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    comment_reply = CommentReplySerializer(many = True)
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = [
            'user',
            'body',
            'post',
            'comment_reply'
        ]

class CommentCreateSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Like
        fields = '__all__'

class LikeCreateSerializer(ModelSerializer):
    
    class Meta:
        model = Like
        fields = '__all__'

class HashtagSerializer(ModelSerializer):

    class Meta:
        model = Hashtag
        fields = '__all__'

class HashtagPostSerializer(ModelSerializer):
    hashtag = HashtagSerializer()
    class Meta:
        model = HashtagPost
        fields = '__all__'

class HashtagPostCreateSerializer(ModelSerializer):

    class Meta:
        model = HashtagPost
        fields = '__all__'

class PostSerializer(ModelSerializer):

    user = UserSerializer()
    comment = CommentSerializer(many = True)
    hashtag = HashtagPostSerializer(many = True)
    like = LikeSerializer(many = True)

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'image',
            'body',
            'date',
            'like',
            'comment',
            'hashtag'
        ]

class PostCreateSerializer(ModelSerializer):

    def __init__(self, *args, **kwargs):

        context = kwargs.get('context', None)
        if context:
           self.user = context['user'] 

        super().__init__(*args, **kwargs)
        
    def validate(self, data):

        if data['user'] != self.user:
            raise serializers.ValidationError("cannot create post for other users !")
        return data

    class Meta:
        model = Post
        fields = '__all__'

class PostBriefSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'image']


class UserProfileSerializer(ModelSerializer):

    followers = SerializerMethodField('get_followers')
    followings = SerializerMethodField('get_followings')
    posts = SerializerMethodField('get_posts')

    class Meta:

        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'image',
            'phone_number',
            'bio',
            'followers',
            'followings',
            'posts',
        ]

    def get_followers(self, obj):

        username = obj.username
        print('user username')
        obj_ = Follow.objects.filter(followed__username = username).count()
        return obj_

    def get_followings(self, obj):

        username = obj.username
        print('user username')
        obj_ = Follow.objects.filter(follower__username = username).count()
        return obj_

    def get_posts(self, obj):

        username = obj.username
        obj_ = Post.objects.filter(user__username = username)
        print(obj_)
        ser_obj = PostBriefSerializer(obj_, many = True)
        return ser_obj.data

class PostCommentsSerializer(ModelSerializer):

    comment = CommentSerializer(many = True) 

    class Meta:
        model = Post
        fields = ['comment', ]