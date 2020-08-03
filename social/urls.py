from django.contrib import admin
from django.urls import path, include
from shop import views as shop_view
from social_media import views as social_media_view
from test1 import views as test1_view
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "King's Social Media"
admin.site.index_title = 'Social Media Project Details'

urlpatterns = [
    path('admin/', admin.site.urls),
    #? inja ham faghat marboot be social medias:
    #! Follow:
    path('follow/', social_media_view.FollowListCreateView.as_view()),
    path('follow/<int:pk>', social_media_view.FollowDetailUpdateDeleteAPIView.as_view()),
    #! Post:
    path('post/', social_media_view.PostListCreateView.as_view()),
    path('post/<int:pk>', social_media_view.PostDetailUpdateDeleteAPIView.as_view()),
    #! Like:
    path('like/', social_media_view.LikeListCreateView.as_view()),
    path('like/<int:pk>', social_media_view.LikeDetailUpdateDeleteAPIView.as_view()),
    #! Comment:
    path('comment/', social_media_view.CommentListCreateView.as_view()),
    path('comment/<int:pk>', social_media_view.CommentDetailUpdateDeleteAPIView.as_view()),
    #! CommentReply:
    path('commentreply/', social_media_view.CommentReplyListCreateView.as_view()),
    path('commentreply/<int:pk>', social_media_view.CommentReplyDetailUpdateDeleteAPIView.as_view()),
    #! Hashtag:
    path('hashtag/', social_media_view.HashtagListCreateView.as_view()),
    path('hashtag/<int:pk>', social_media_view.HashtagDetailUpdateDeleteAPIView.as_view()),
    #! HashtagPost:
    path('hashtagpost/', social_media_view.HashtagPostListCreateView.as_view()),
    path('hashtagpost/<int:pk>', social_media_view.HashtagPostDetailUpdateDeleteAPIView.as_view()),
    #TODO:
    #? for custom api views:
    path('firstpage/', social_media_view.UserFirstPage.as_view()),
    path('delete_like/', social_media_view.DeleteLikeOfPost.as_view()),
    path('userprofilepage/<str:pk>/', social_media_view.UserProfilePage.as_view()),
    path('postcomments/<int:pk>/', social_media_view.PostComments.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)