from django.contrib import admin

from .models import Project_request, Project_ask_request, Website_error_request, Other_request

# Register your models here.

admin.site.register(Project_request)
admin.site.register(Project_ask_request)
admin.site.register(Website_error_request)
admin.site.register(Other_request)
