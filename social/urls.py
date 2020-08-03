from django.contrib import admin
from django.urls import path, include
from test1.views import *
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "King's Social Media"
admin.site.index_title = 'Social Media Project Details'

urlpatterns = [
    path('admin/', admin.site.urls),
    #? inja ham faghat marboot be social medias:
    #! Follow:
    path('follow/', FollowListCreateView.as_view()),
    path('follow/<int:pk>', FollowDetailUpdateDeleteAPIView.as_view()),
    #! Post:
    path('post/', PostListCreateView.as_view()),
    path('post/<int:pk>', PostDetailUpdateDeleteAPIView.as_view()),
    #! Like:
    path('like/', LikeListCreateView.as_view()),
    path('like/<int:pk>', LikeDetailUpdateDeleteAPIView.as_view()),
    #! Comment:
    path('comment/', CommentListCreateView.as_view()),
    path('comment/<int:pk>', CommentDetailUpdateDeleteAPIView.as_view()),
    #! CommentReply:
    path('commentreply/', CommentReplyListCreateView.as_view()),
    path('commentreply/<int:pk>', CommentReplyDetailUpdateDeleteAPIView.as_view()),
    #! Hashtag:
    path('hashtag/', HashtagListCreateView.as_view()),
    path('hashtag/<int:pk>', HashtagDetailUpdateDeleteAPIView.as_view()),
    #! HashtagPost:
    path('hashtagpost/', HashtagPostListCreateView.as_view()),
    path('hashtagpost/<int:pk>', HashtagPostDetailUpdateDeleteAPIView.as_view()),
    #TODO:
    #? for custom api views:
    path('firstpage/', UserFirstPage.as_view()),
    path('delete_like/', DeleteLikeOfPost.as_view()),
    path('userprofilepage/<str:pk>/', UserProfilePage.as_view()),
    path('postcomments/<int:pk>/', PostComments.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)