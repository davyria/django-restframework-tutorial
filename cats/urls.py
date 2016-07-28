from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from cats import views

urlpatterns = [
    url(r'^cats/$', views.CatList.as_view()),
    url(r'^cats/(?P<pk>[0-9]+)/$', views.CatDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)