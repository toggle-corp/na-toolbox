from django.conf.urls import url, static
from django.contrib import admin
from django.conf import settings

from toolbox.views import HomeView, ToolListView, DownloadFiles


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^download/$', DownloadFiles.as_view(), name='download'),

    url(r'^(?P<slug>[\w-]+)/$', ToolListView.as_view(), name='tool_list'),
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
