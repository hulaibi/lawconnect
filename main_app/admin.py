from django.contrib import admin
from .models import Case
# Register your models here.


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'status', 'created_at')
    search_fields = ('title', 'description', 'user__username')
    list_filter = ('category', 'status', 'created_at')
    ordering = ('-created_at',)
    
    