from django.contrib import admin
from django.urls import path, include
from shop import views as shop_view
from social_media import views as social_media_view
from test1 import views as test1_view
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "King's Muscle Media"
admin.site.index_title = 'Muscle Media Project Details'

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)