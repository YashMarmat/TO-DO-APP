from django.shortcuts import render
from .models import Schedule
from django.urls import reverse_lazy
from django.views.generic import ListView


from django.views.generic.edit import(
    CreateView,
    UpdateView,
    DeleteView,
)


class ScheduleList(ListView):
    model         = Schedule 
    template_name = 'home.html'


class ScheduleCreate(CreateView):
    model         = Schedule
    template_name = "schedule_create.html"
    fields        = '__all__'
    success_url   = reverse_lazy('home')

class ScheduleUpdate(UpdateView):
    model         = Schedule
    template_name = "schedule_update.html"
    fields        = '__all__'
    success_url   = reverse_lazy('home')

class ScheduleDelete(DeleteView):
    model = Schedule
    template_name = "schedule_delete.html"
    success_url   = reverse_lazy('home')