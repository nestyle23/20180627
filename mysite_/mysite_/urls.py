

from django.contrib import admin
from django.conf.urls import include,url
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
     url(r'^blog/', include('blog.urls')),   
     url(r'^admin/', admin.site.urls),
     url(r'^tour/', include('tour.urls')),  
     url(r'^$', include('tour.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)