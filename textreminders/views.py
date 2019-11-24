from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Reminder

class ReminderCreateView(SuccessMessageMixin, CreateView):
    model = Reminder
    fields = ['name', 'phone_number', 'time', 'time_zone']
    success_message = 'Reminder successfully created.'

class ReminderDetailView(DetailView):
    model = Reminder

class ReminderListView(ListView):
    model = Reminder

class ReminderUpdateView(SuccessMessageMixin, UpdateView):
    model = Reminder
    fields = ['name', 'phone_number', 'time', 'time_zone']
    success_message = 'Reminder successfully updated.'


class ReminderDeleteView(DeleteView):
    model = Reminder
    success_url = reverse_lazy('list_reminder')