from django.contrib import admin
from core.models import product

# Register your models here.
class productadmin(admin.ModelAdmin):
    list_display=('name','price','desc','url')


admin.site.register(product,productadmin)