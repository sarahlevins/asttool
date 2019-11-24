from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from timezone_field import TimeZoneField
from django.urls import reverse


@python_2_unicode_compatible
class Reminder(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    time = models.DateTimeField()
    time_zone = TimeZoneField(default='Australia/Perth')

    # Additional fields not visible to users
    task_id = models.CharField(max_length=50, blank=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Reminder #{0} - {1}'.format(self.pk, self.name)
    
    def get_absolute_url(self):
        return reverse('view_reminder', args=[str(self.id)])

