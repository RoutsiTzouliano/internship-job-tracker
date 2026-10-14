from django.contrib import admin

# Register your models here.
from .models import Application, Company, JobPosting 

admin.site.register(Application)
admin.site.register(Company)
admin.site.register(JobPosting)