from django.contrib import admin
from .models import JPuser

# Register your models here.

class JPuserAdmin(admin.ModelAdmin):
    pass

admin.site.register(JPuser, JPuserAdmin)