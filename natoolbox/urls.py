from django.conf.urls import include, url, static
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

from toolbox.views import HomeView, ToolListView, \
    DownloadFiles, FaqsView, \
    NetworkAndContactView
from field_support.views import FieldSupportView


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^field-support/$', FieldSupportView.as_view(), name='field_support'),
    url(r'^network-and-contact/$', NetworkAndContactView.as_view(), name='network_and_contact'),

    url(r'^download/$', DownloadFiles.as_view(), name='download'),
    url(r'^faqs/$', FaqsView.as_view(), name='faqs'),
    url(r'^downloading/$', TemplateView.as_view(
        template_name='toolbox/downloading.html'), name='downloading'),

    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^(?P<slug>[\w-]+)/$', ToolListView.as_view(), name='tool_list'),
] + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
