from django.contrib import admin
from .models import Task, Who

# Register your models here.

class DisplayTask(admin.ModelAdmin):
    list_display = ('id', 'title', 'status')
    list_display_links = ('id', 'title')
    list_filter = ('status', )
    list_per_page = 10
    list_editable = ('status', )

class DisplayWho(admin.ModelAdmin):
    list_display = ('id','firstName')
    list_display_links = ('id', 'firstName')
    list_per_page = 10


admin.site.register(Task, DisplayTask)
admin.site.register(Who, DisplayWho)