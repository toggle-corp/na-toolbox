from django.conf.urls import url
from django.contrib import admin

from toolbox.views import HomeView, ToolsAndTemplatesView


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^tools-and-templates/$', ToolsAndTemplatesView.as_view(), name='tools_and_templates'),
]
