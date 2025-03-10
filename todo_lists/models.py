from django.db import models

# Create your models here.
class Project(models.Model):
    """
    Project model to organize todo lists and tasks.
    
    Attributes:
        title: The title of the project
        description: Detailed description of the project
        created_at: Timestamp when the project was created
        updated_at: Timestamp when the project was last updated
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """String representation of the Project model."""
        return self.title
    
    class Meta:
        ordering = ['-created_at']
