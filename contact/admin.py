from django.contrib import admin
from contact.models import Contact, Category

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'show', #type: ignore
    ordering = 'id', #type: ignore
    #list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name', #type: ignore
    list_per_page = 10
    list_editable = 'first_name', 'last_name', 'show', #type: ignore

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id', #type: ignore