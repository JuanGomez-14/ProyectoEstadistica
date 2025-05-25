from django.contrib import admin
from .models import ExcelFile

@admin.register(ExcelFile)
class ExcelFileAdmin(admin.ModelAdmin):
    list_display = ('file', 'user', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('file', 'user__username')