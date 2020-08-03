from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(CommentReply)
admin.site.register(Hashtag)
admin.site.register(HashtagPost)

class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('username', 'phone_number', 'is_active')
    search_fields = ('username', 'phone_number', )

admin.site.unregister(Group)
admin.site.register(CustomUser, CustomUserAdmin)