from django.conf.urls import include,url
from . import views


urlpatterns = [
     url(r'^$', views.main_grid, name='main_grid'),
]