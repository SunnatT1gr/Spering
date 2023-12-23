from django.shortcuts import render
from django.views.generic import TemplateView

def homeview(request):
    return render(request, 'index.html')

class WorkView(TemplateView):
    template_name = 'work.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class CategoryView(TemplateView):
    template_name = 'category.html'