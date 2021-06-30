from django.contrib import admin
from .models import Jpuser

# Register your models here.

class JpuserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'registered_dttm')

admin.site.register(Jpuser, JpuserAdmin)