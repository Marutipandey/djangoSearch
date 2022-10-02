from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','roll','address']