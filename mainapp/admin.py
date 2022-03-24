from django.contrib import admin
from mainapp import models

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'email', 'phone', 'height_cms')
    list_display_links = ('id', 'user', 'full_name',
                          'email', 'phone', 'height_cms')
    search_fields = ('id', 'full_name')
    list_per_page = 20


# class SessionAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'session_date',
#                     'session_startTime', 'session_endTime', 'session_slouches')
#     list_display_links = ('id', 'user', 'session_date',
#                           'session_startTime', 'session_endTime', 'session_slouches')
#     search_fields = ('id', 'user')
#     list_per_page = 20


admin.site.register(models.Profile, ProfileAdmin)
# admin.site.register(models.Session, SessionAdmin)
