from django.contrib import admin
from .models import Project, Task

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin configuration for the Project model."""
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """Admin configuration for the Task model."""
    list_display = ('title', 'due_date', 'is_completed', 'project', 'created_at')
    list_filter = ('is_completed', 'due_date', 'created_at', 'project')
    search_fields = ('title', 'description')
    date_hierarchy = 'due_date'
    list_editable = ('is_completed',)
