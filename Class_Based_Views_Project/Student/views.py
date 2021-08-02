from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from Student.models import StudentData
from django.urls import reverse, reverse_lazy

# Create your views here.
class StudentList_View(ListView):
    model = StudentData

class StudentDetails_View(DetailView):
    model = StudentData

class StudentCreate_View(CreateView):
    model = StudentData
    fields = ('firstName','lastName','percentage','standard')

class StudentUpdate_View(UpdateView):
    model = StudentData
    fields = ('standard',)

class StudentDelete_View(DeleteView):
    model = StudentData
    success_url = reverse_lazy('students')