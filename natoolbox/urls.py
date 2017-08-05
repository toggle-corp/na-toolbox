from django.conf.urls import url, static
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

from toolbox.views import HomeView, ToolListView, DownloadFiles, ContactUsView


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'^download/$', DownloadFiles.as_view(), name='download'),
    url(r'^contact-us/$', ContactUsView.as_view(), name='contact_us'),
    url(r'^downloading/$', TemplateView.as_view(
        template_name='toolbox/downloading.html'), name='downloading'),

    url(r'^(?P<slug>[\w-]+)/$', ToolListView.as_view(), name='tool_list'),
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
