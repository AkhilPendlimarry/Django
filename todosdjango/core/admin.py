from django.contrib import admin
from core.models import todo

# Register your models here.
class todoadmin(admin.ModelAdmin):
    list_display = ("task",)
class productadmin(admin.ModelAdmin):
    list_display = ("name","price", "desc", "url", )

admin.site.register(todo, todoadmin) # todo= model, todoadmin = admin interface
