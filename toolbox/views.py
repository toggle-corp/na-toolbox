from django.shortcuts import render
from django.views.generic import View


class HomeView(View):
    def get(self, request):
        context = {}
        return render(request, 'toolbox/home.html', context)


class ToolsAndTemplatesView(View):
    def get(self, request):
        context = {}
        return render(request, 'toolbox/tools-and-templates.html', context)


class ContactUsView(View):
    def get(self, request):
        context = {}
        return render(request, 'toolbox/contact-us.html', context)
