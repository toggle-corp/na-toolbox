from django.shortcuts import render
from django.views.generic import View
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
