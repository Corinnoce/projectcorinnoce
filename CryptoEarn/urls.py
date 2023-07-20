from django.contrib import admin
from django.urls import path,include
from .views import index,newsletter
from CryptoEarn import settings
from django.conf.urls.static import static
#from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('blogs/',include('blogs.urls')),
    path('user/',include('accounts.urls')),
    path('community/',include('community.urls')),
    path('newsletters/register/',newsletter,name="newsletter"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#handler404="CryptoEarn.views.NotFound"
