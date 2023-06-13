from django.contrib import admin
from .models import Jobs

# Register your models here.
class JobsModelAdmin(admin.ModelAdmin):
    List_display=['jobid', 'title', 'skills', 'description']
    Last_filter=['title']

    class Meta:
        model=Jobs
admin.site.register(Jobs,JobsModelAdmin)

