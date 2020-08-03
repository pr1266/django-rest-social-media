from django.db import models
from django.contrib.auth.models import AbstractUser
import os


def user_post_directory_path(instance, file_name):

    return 'posts/user_{0}/{1}'.format(instance.user.username, file_name)


class CustomUser(AbstractUser):

    username     = models.CharField(max_length = 250, primary_key = True)
    password     = models.CharField(max_length = 250)
    phone_number = models.CharField(max_length = 250)
    last_visit   = models.DateTimeField(null = True, blank = True)
    image        = models.ImageField(upload_to = user_directory_path, null = True) 
    bio          = models.CharField(max_length = 250, null = True)
    
    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email',]

    def __str__(self):

        return self.username

class Follow(models.Model):

    follower = models.ForeignKey(CustomUser, on_delete = models.CASCADE, null = True, related_name = 'follower')
    followed = models.ForeignKey(CustomUser, on_delete = models.CASCADE, null = True, related_name = 'following')
    date = models.DateTimeField(auto_now = True)

    def __str__(self):

        return self.follower.username + ' ' + self.followed.username

class Post(models.Model):

    user = models.ForeignKey(CustomUser, related_name = 'posts', on_delete = models.CASCADE, null = True)
    image = models.ImageField(null = True, upload_to = user_post_directory_path)
    body = models.TextField()
    date = models.DateTimeField(auto_now = True)

    def __str__(self):

        return self.user.username + str(self.date)

class Like(models.Model):

    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, related_name = 'like', on_delete = models.CASCADE)

    class Meta:
        unique_together = ['user', 'post']

    def __str__(self):

        return self.user.username + str(self.post.id)

class Comment(models.Model):

    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, null = True)
    body = models.TextField()
    post = models.ForeignKey(Post, related_name = 'comment', on_delete = models.CASCADE, null = True)

    def __str__(self):

        return self.user.username + str(self.post.id)

class CommentReply(models.Model):

    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE, null = True)
    body = models.TextField()
    comment = models.ForeignKey(Comment, related_name = 'comment_reply', on_delete = models.CASCADE, null = True)

    def __str__(self):

        return self.user.username + str(self.comment.id)

class Hashtag(models.Model):

    name = models.CharField(max_length = 100)

    def __str__(self):

        return self.name

class HashtagPost(models.Model):

    hashtag = models.ForeignKey(Hashtag, on_delete = models.CASCADE, null = True)
    post = models.ForeignKey(Post, related_name = 'hashtag', on_delete = models.CASCADE, null = True)

    class Meta:
        unique_together = ['hashtag', 'post']

    def __str__(self):

        return self.hashtag.name + str(self.post.id)