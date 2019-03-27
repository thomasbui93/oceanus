from django.contrib import admin

# Register your models here.
from .models.api_key import ApiKey
from .models.project import Project

admin.site.register(Project)
admin.site.register(ApiKey)