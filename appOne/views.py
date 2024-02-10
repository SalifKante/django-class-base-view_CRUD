from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy

from . import models
# Create your views here.

# def index(request):
#     return render(request, 'index.html')

# class CBView(View):

#     def get(self, request):
#         return HttpResponse("Hi") 

# class IndexView(TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['injectme'] = 'INJECTION!!!'
#         return context

class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    # return 'school_list' by default
    context_object_name = 'schools' #change in your own name
    model = models.School

class SchoolDetailView(DetailView):
    # return 'school' by default
    context_object_name = 'school_detail' #change in your own name
    model = models.School
    template_name = 'appOne/school_detail.html'


class SchoolCreateView(CreateView):
    fields=('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('app_one:list')
    
    
    