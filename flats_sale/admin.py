from django.contrib import admin
from flats_sale.models import Flat, Object, Category, Floor


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ("object_name",)
    search_fields = ("foreignkey__object_name", "text")
    
    
@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name", "text")
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "object_name")
    search_fields = ("name",)

@admin.register(Floor)
class FloorAdmin(admin.ModelAdmin):
    list_display = ('number',)