from django.contrib import admin
from .models import Meeting
from .models import Room

# Register your models here.

#admin.site.register(Meeting)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['name', 'floor','room_number']


#class ModuleInline(admin.StackedInline):
   # model = Room


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'start_time', 'duration']
    list_filter = ['room']
   # inlines = [ModuleInline]