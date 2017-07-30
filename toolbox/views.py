from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from io import BytesIO
from zipfile import ZipFile
import json
import urllib
import os

from toolbox.models import ToolList


class HomeView(View):
    def get(self, request):
        context = {}
        context['tool_lists'] = ToolList.objects.all()
        return render(request, 'toolbox/home.html', context)


class ToolListView(View):
    def get(self, request, slug):
        context = {}
        context['tool_lists'] = ToolList.objects.all()
        context['current_list'] = ToolList.objects.get(slug=slug)
        return render(request, 'toolbox/tool-list.html', context)


class DownloadFiles(View):
    def post(self, request):
        mem = BytesIO()
        zip = ZipFile(mem, 'a')

        urls = json.loads(request.POST.get('urls'))
        for i, url in enumerate(urls):
            file = urllib.request.urlopen(url)
            name = ''
            try:
                name = file.info()['Content-Disposition']
                if not name:
                    raise Exception()
            except:
                name = os.path.basename(
                    urllib.parse.urlsplit(file.geturl()).path)

            if not name:
                name = 'download-{}'.format(i)
            zip.writestr(name, file.read())

        for file in zip.filelist:
            file.create_system = 0
        zip.close()

        response = HttpResponse(content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename=download.zip'

        mem.seek(0)
        response.write(mem.read())

        return response
