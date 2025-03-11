from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Project, Task

# Create your views here.
def index(request):
    """
    View function for the home page of the site.
    
    Displays a list of projects and their related tasks.
    """
    # Get all projects and tasks
    projects = Project.objects.all()
    tasks = Task.objects.filter(is_completed=False)
    
    # Count completed and pending tasks
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(is_completed=True).count()
    
    context = {
        'projects': projects,
        'tasks': tasks,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
    }
    
    return render(request, 'todo_lists/index.html', context)

# Project views
def project_list(request):
    """View to display all projects."""
    projects = Project.objects.all()
    return render(request, 'todo_lists/project_list.html', {'projects': projects})

def project_detail(request, pk):
    """View to display details of a specific project."""
    project = get_object_or_404(Project, pk=pk)
    tasks = Task.objects.filter(project=project)
    return render(request, 'todo_lists/project_detail.html', {'project': project, 'tasks': tasks})

def project_create(request):
    """View to create a new project."""
    if request.method == 'POST':
        # Process the form data
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        
        if title:
            # Create a new project
            project = Project.objects.create(
                title=title,
                description=description
            )
            return redirect('todo_lists:project_detail', pk=project.id)
    
    # Display the empty form
    return render(request, 'todo_lists/project_form.html')

def project_update(request, pk):
    """View to update an existing project."""
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        # Process the form data
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        
        if title:
            # Update the project
            project.title = title
            project.description = description
            project.save()
            return redirect('todo_lists:project_detail', pk=project.id)
    
    # Display the form with the current data
    return render(request, 'todo_lists/project_form.html', {'project': project})

def project_delete(request, pk):
    """View to delete a project."""
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        # Delete the project
        project.delete()
        return redirect('todo_lists:project_list')
    
    # Display the confirmation page
    return render(request, 'todo_lists/project_confirm_delete.html', {'project': project})

# Task views
def task_list(request):
    """View to display all tasks."""
    tasks = Task.objects.all()
    return render(request, 'todo_lists/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    """View to display details of a specific task."""
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'todo_lists/task_detail.html', {'task': task})

def task_create(request):
    """View to create a new task."""
    if request.method == 'POST':
        # Process the form data
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        project_id = request.POST.get('project', '')
        due_date_str = request.POST.get('due_date', '')
        is_completed = request.POST.get('is_completed', False) == 'on'
        
        if title:
            # Create a new task
            task = Task(
                title=title,
                description=description,
                is_completed=is_completed
            )
            
            # Set project if selected
            if project_id:
                task.project = get_object_or_404(Project, pk=project_id)
                
            # Set due date if provided
            if due_date_str:
                task.due_date = due_date_str
                
            task.save()
            return redirect('todo_lists:task_detail', pk=task.id)
    
    # Get all projects for the form's project selection dropdown
    projects = Project.objects.all()
    
    # Display the empty form
    return render(request, 'todo_lists/task_form.html', {'projects': projects})

def task_update(request, pk):
    """View to update an existing task."""
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        # Process the form data
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        project_id = request.POST.get('project', '')
        due_date_str = request.POST.get('due_date', '')
        is_completed = request.POST.get('is_completed', False) == 'on'
        
        if title:
            # Update the task
            task.title = title
            task.description = description
            task.is_completed = is_completed
            
            # Set project if selected, otherwise set to None
            if project_id:
                task.project = get_object_or_404(Project, pk=project_id)
            else:
                task.project = None
                
            # Set due date if provided, otherwise set to None
            if due_date_str:
                task.due_date = due_date_str
            else:
                task.due_date = None
                
            task.save()
            return redirect('todo_lists:task_detail', pk=task.id)
    
    # Get all projects for the form's project selection dropdown
    projects = Project.objects.all()
    
    # Display the form with the current data
    return render(request, 'todo_lists/task_form.html', {'task': task, 'projects': projects})

def task_delete(request, pk):
    """View to delete a task."""
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        # Delete the task
        task.delete()
        return redirect('todo_lists:task_list')
    
    # Display the confirmation page
    return render(request, 'todo_lists/task_confirm_delete.html', {'task': task})

def task_toggle_completion(request, pk):
    """Toggle the completion status of a task."""
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('todo_lists:index')))
