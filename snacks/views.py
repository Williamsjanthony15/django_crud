# from django.shortcuts import render
from .models import Snack
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView, CreateView, DetailView, ListView


# Create your views here.
class SnackListView(ListView):
    template_name = 'snackList.html'
    model = Snack
    success_url = reverse_lazy('listView')

class SnackDetailView(DetailView):
    template_name = 'snackDetail.html'
    model = Snack
    success_url = reverse_lazy('listView')

class SnackCreateView(CreateView):
    template_name = 'snackCreate.html'
    model = Snack
    fields = ['title', 'description', 'purchaser' ]
    success_url = reverse_lazy('listView')

class SnackDeleteView(DeleteView):
    template_name = 'snackDelete.html'
    model = Snack
    success_url = reverse_lazy('listView')

class SnackUpdateView(UpdateView):
    template_name = 'snackUpdate.html'
    model = Snack
    fields = ['title', 'description', 'purchaser' ]
    success_url = reverse_lazy('listView')