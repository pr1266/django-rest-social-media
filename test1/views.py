from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .serializers import *
from .permissions import *
from .models import *

#! Follow:
class FollowDetailUpdateDeleteAPIView(APIView):

    def get_object(self, pk):
        
        try:
            return Follow.objects.get(pk = pk)
        except:
            None

    @method_decorator(cache_page(60*60*2))
    def get(self, request, pk):

        Follow = self.get_object(pk)
        if Follow:
            ser_obj = FollowSerializer(Follow, many = False)
            return Response(ser_obj.data)
        return Response(status = status.HTTP_404_NOT_FOUND)

    @method_decorator(cache_page(60*60*2))
    def put(self, request, pk):

        Follow = self.get_object(pk)
        ser_obj = FollowSerializer(Follow, data = request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.data)
        return Response(ser_obj.errors, status = status.HTTP_400_BAD_REQUEST)

    @method_decorator(cache_page(60*60*2))
    def delete(self, request, pk):
        
        Follow = self.get_object(pk)
        Follow.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class FollowListCreateView(ListCreateAPIView):

    def get_serializer_class(self):

        if self.request.method == 'GET':
            return FollowSerializer
        return FollowCreateSerializer

    serializer_class = FollowSerializer
    queryset = Follow.objects.all()

#! POST:
class PostDetailUpdateDeleteAPIView(APIView):

    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    permission_classes = [PostCustomPermission]

    def get_object(self, pk):
        
        try:
            return Post.objects.get(pk = pk)
        except:
            None

    @method_decorator(cache_page(60*60*3))
    def get(self, request, pk):

        post = self.get_object(pk)
        if post:
            ser_obj = PostSerializer(post, many = False)
            return Response(ser_obj.data)
        return Response(status = status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):

        post = self.get_object(pk)
        ser_obj = PostSerializer(post, data = request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.data)
        return Response(ser_obj.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        
        post = self.get_object(pk)
        post.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class PostListCreateView(ListCreateAPIView):

    def get_serializer_context(self):

        context = super().get_serializer_context()
        user = self.request.user
        context['user'] = user

        return context

    def get_serializer_class(self):

        if self.request.method == 'GET':
            return PostSerializer
        return PostCreateSerializer

    serializer_class = PostSerializer
    queryset = Post.objects.all()

#! LIKE:
class LikeDetailUpdateDeleteAPIView(APIView):

    permission_classes = [LikeCustomPermission,]

    def get_object(self, pk):
        
        try:
            return Like.objects.get(pk = pk)
        except:
            None

    def get(self, request, pk):

        like = self.get_object(pk)
        if like:
            ser_obj = LikeSerializer(like, many = False)
            return Response(ser_obj.data)
        return Response(status = status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):

        like = self.get_object(pk)
        ser_obj = LikeSerializer(like, data = request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.data)
        return Response(ser_obj.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        
        like = self.get_object(pk)
        like.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class LikeListCreateView(ListCreateAPIView):

    def get_serializer_class(self):

        if self.request.method == 'GET':
            return LikeSerializer
        return LikeCreateSerializer

    serializer_class = LikeSerializer
    queryset = Like.objects.all()

#! Comment:
class CommentDetailUpdateDeleteAPIView(APIView):

    def get_object(self, pk):
        
        try:
            return Comment.objects.get(pk = pk)
        except:
            None

    def get(self, request, pk):

        comment = self.get_object(pk)
        if comment:
            ser_obj = CommentSerializer(comment, many = False)
            return Response(ser_obj.data)
        return Response(status = status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):

        comment = self.get_object(pk)
        ser_obj = CommentSerializer(comment, data = request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.data)
        return Response(ser_obj.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        
        comment = self.get_object(pk)
        comment.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class CommentListCreateView(ListCreateAPIView):

    def get_serializer_class(self):

        if self.request.method == 'GET':
            return CommentSerializer
        return CommentCreateSerializer

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

#! CommentReply:
class CommentReplyDetailUpdateDeleteAPIView(APIView):

    def get_object(self, pk):
        
        try:
            return CommentReply.objects.get(pk = pk)
        except:
            None

    def get(self, request, pk):

        commentReply = self.get_object(pk)
        if commentReply:
            ser_obj = CommentReplySerializer(commentReply, many = False)
            return Response(ser_obj.data)
        return Response(status = status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):

        commentReply = self.get_object(pk)
        ser_obj = CommentReplySerializer(commentReply, data = request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.data)
        return Response(ser_obj.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        
        commentReply = self.get_object(pk)
        commentReply.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class CommentReplyListCreateView(ListCreateAPIView):

    def get_serializer_class(self):

        if self.request.method == 'GET':
            return CommentReplySerializer
        return CommentReplyCreateSerializer

    serializer_class = CommentReplySerializer
    queryset = CommentReply.objects.all()

#! Hashtag:
class HashtagDetailUpdateDeleteAPIView(APIView):

    def get_object(self, pk):
        
        try:
            return Hashtag.objects.get(pk = pk)
        except:
            None

    def get(self, request, pk):

        hashtag = self.get_object(pk)
        if hashtag:
            ser_obj = HashtagSerializer(hashtag, many = False)
            return Response(ser_obj.data)
        return Response(status = status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):

        hashtag = self.get_object(pk)
        ser_obj = HashtagSerializer(hashtag, data = request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.data)
        return Response(ser_obj.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        
        hashtag = self.get_object(pk)
        hashtag.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class HashtagListCreateView(ListCreateAPIView):

    serializer_class = HashtagSerializer
    queryset = Hashtag.objects.all()

#! HashtagPost:
class HashtagPostDetailUpdateDeleteAPIView(APIView):

    def get_object(self, pk):
        
        try:
            return HashtagPost.objects.get(pk = pk)
        except:
            None

    def get(self, request, pk):

        hashtagPost = self.get_object(pk)
        
        if hashtagPost:
        
            ser_obj = HashtagPostSerializer(hashtagPost, many = False)
            return Response(ser_obj.data)
        
        return Response(status = status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):

        hashtagPost = self.get_object(pk)
        ser_obj = HashtagPostSerializer(hashtagPost, data = request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            return Response(ser_obj.data)
        return Response(ser_obj.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        
        hashtagPost = self.get_object(pk)
        hashtagPost.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class HashtagPostListCreateView(ListCreateAPIView):

    def get_serializer_class(self):
        
        if self.request.method == 'POST':
            return HashtagPostCreateSerializer
        return HashtagPostSerializer

    serializer_class = HashtagPostSerializer
    queryset = HashtagPost.objects.all()

#! Custome api views :
class UserFirstPage(APIView):

    def get_object(self, user):

        return Follow.objects.filter(follower__username = user)

    def get_post(self, obj):

        return Post.objects.filter(user__username__in = obj.values('followed'))

    def get(self, request):

        user = request.user.username
        obj = self.get_object(user)
        obj_ = self.get_post(obj)
        print('posts : ')
        print(obj_)
        ser_obj = PostSerializer(obj_, many = True)
        return Response(ser_obj.data)

#! delete like of post:
class DeleteLikeOfPost(APIView):

    def post(self, request):

        username = request.data['username']
        post = request.data['post']

        print(username)
        print(post)

        obj = Like.objects.filter(Q(user__username = username) & Q(post__id = post))
        print(obj)
        obj.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

#! user profile page
class UserProfilePage(APIView):

    def get_object(self, pk):

        return CustomUser.objects.get(pk = pk)

    def get(self, request, pk):

        obj = self.get_object(pk)
        ser_obj = UserProfileSerializer(obj, many = False)

        return Response(ser_obj.data, status = status.HTTP_200_OK)

#! Comments of a post:

class PostComments(APIView):

    def get(self, reqeust, pk):
        
        obj = Post.objects.get(pk = pk)
        ser_obj = PostCommentsSerializer(obj)
        return Response(ser_obj.data)
