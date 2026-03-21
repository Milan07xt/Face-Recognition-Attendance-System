from django.contrib import admin
from .models import AttendanceRecord

@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'timestamp', 'status', 'subject')
    list_filter = ('status', 'subject', 'timestamp')
    search_fields = ('name', 'subject')
    ordering = ('-timestamp',)
    readonly_fields = ('timestamp',)
