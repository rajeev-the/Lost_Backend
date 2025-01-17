from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ApiData

# Register your models here.

class ApiDataAdmin(admin.ModelAdmin):
    list_display = ['name', 'found', 'data', 'time', 'location']  # Display these fields in the admin list view
    list_filter = ['found', 'data', 'location']  # Add filters for these fields
    search_fields = ['name', 'description', 'location']  # Enable search on these fields
    date_hierarchy = 'created_at'  # Add a date-based drill-down navigation sidebar
    readonly_fields = ['created_at']  # Mark 'created_at' field as read-only in admin

admin.site.register(ApiData, ApiDataAdmin)

