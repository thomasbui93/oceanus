from django.db import models
from .project import Project

class ApiKey(models.Model):
    key = models.TextField(primary_key=True)
    description = models.TextField()
    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
        verbose_name="associated_project",
    )
    created_at = models.DateTimeField(auto_now_add=True,
                                      editable=False)
    updated_at = models.DateTimeField(auto_now=True,
                                      editable=False)