from django.contrib import admin
from app1.models import *

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('user','firstname','lastname','email','mobile','state','dob','gender','address')
    search_fields = ('name',)
     
admin.site.register(Blog,BlogAdmin)


