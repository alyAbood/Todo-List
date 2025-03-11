from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    """
    Project model to organize todo lists and tasks.
    
    Attributes:
        title: The title of the project
        description: Detailed description of the project
        user: The user who owns this project
        created_at: Timestamp when the project was created
        updated_at: Timestamp when the project was last updated
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """String representation of the Project model."""
        return self.title
    
    class Meta:
        ordering = ['-created_at']


class Task(models.Model):
    """
    Task model to manage individual tasks within projects.
    
    Attributes:
        title: The title of the task
        description: Detailed description of the task
        due_date: The deadline for completing the task
        is_completed: Boolean indicating whether the task is completed
        project: Foreign key to the Project model (optional)
        created_at: Timestamp when the task was created
        updated_at: Timestamp when the task was last updated
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE, 
        related_name='tasks',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """String representation of the Task model."""
        return self.title
    
    class Meta:
        ordering = ['due_date', '-created_at']
