from django.conf.urls import re_path

from .views import (
    ReminderCreateView, 
    ReminderDetailView,
    ReminderListView,
    ReminderUpdateView,
    ReminderDeleteView
)

urlpatterns = [
    re_path(r'^$', ReminderListView.as_view(), name='list_reminder'),
    re_path(r'^new$', ReminderCreateView.as_view(), name='new_reminder'),
    re_path(r'^(?P<pk>[0-9]+)$', ReminderDetailView.as_view(), name='view_reminder'),
    re_path(r'^(?P<pk>[0-9]+)/edit$', ReminderUpdateView.as_view(), name='edit_reminder'),
    re_path(r'^(?P<pk>[0-9]+)/delete$', ReminderDeleteView.as_view(), name='delete_reminder'),
]
