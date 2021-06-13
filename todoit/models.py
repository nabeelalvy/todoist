from django.db import models
from django.utils import timezone


class Section(models.Model):
    section_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)


class Todoit(models.Model):
    task_name = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)