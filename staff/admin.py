from django.contrib import admin
from staff.models import Post, Staff

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    
    
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("first_name","name", "last_name", "post_name")
    search_fields = ("first_name","name", "last_name", "post_name")
    