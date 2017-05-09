from django.conf.urls import url
from yblog.views import BlogView


urlpatterns = {
    url(r'^$', BlogView.as_view(), name='index')
}