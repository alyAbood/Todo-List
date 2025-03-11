from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Project, Task

# Create your views here.
@login_required
def index(request):
    """
    View function for the home page of the site.
    
    Displays a list of projects and their related tasks for the logged-in user.
    """
    # Get user's projects and tasks
    projects = Project.objects.filter(user=request.user)
    tasks = Task.objects.filter(project__user=request.user, is_completed=False)
    
    # Count completed and pending tasks for the user
    total_tasks = Task.objects.filter(project__user=request.user).count()
    completed_tasks = Task.objects.filter(project__user=request.user, is_completed=True).count()
    
    context = {
        'projects': projects,
        'tasks': tasks,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
    }
    
    return render(request, 'todo_lists/index.html', context)

# Project views
@login_required
def project_list(request):
    """View to display all projects for the logged-in user."""
    projects = Project.objects.filter(user=request.user)
    return render(request, 'todo_lists/project_list.html', {'projects': projects})

@login_required
def project_detail(request, pk):
    """View to display details of a specific project owned by the logged-in user."""
    project = get_object_or_404(Project, pk=pk)
    
    # Check if the project belongs to the logged-in user
    if project.user != request.user:
        raise Http404("Project not found")
        
    tasks = Task.objects.filter(project=project)
    return render(request, 'todo_lists/project_detail.html', {'project': project, 'tasks': tasks})

@login_required
def project_create(request):
    """View to create a new project for the logged-in user."""
    if request.method == 'POST':
        # Process the form data
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        
        if title:
            # Create a new project associated with the logged-in user
            project = Project.objects.create(
                title=title,
                description=description,
                user=request.user
            )
            return redirect('todo_lists:project_detail', pk=project.pk)
    
    return render(request, 'todo_lists/project_form.html')

@login_required
def project_update(request, pk):
    """View to update an existing project owned by the logged-in user."""
    project = get_object_or_404(Project, pk=pk)
    
    # Check if the project belongs to the logged-in user
    if project.user != request.user:
        raise Http404("Project not found")
        
    if request.method == 'POST':
        # Process the form data
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        
        if title:
            # Update the project
            project.title = title
            project.description = description
            project.save()
            return redirect('todo_lists:project_detail', pk=project.pk)
    
    return render(request, 'todo_lists/project_form.html', {'project': project})

@login_required
def project_delete(request, pk):
    """View to delete a project owned by the logged-in user."""
    project = get_object_or_404(Project, pk=pk)
    
    # Check if the project belongs to the logged-in user
    if project.user != request.user:
        raise Http404("Project not found")
        
    if request.method == 'POST':
        project.delete()
        return redirect('todo_lists:project_list')
    
    return render(request, 'todo_lists/project_confirm_delete.html', {'project': project})

# Task views
@login_required
def task_list(request):
    """View to display all tasks for the logged-in user."""
    tasks = Task.objects.filter(project__user=request.user)
    return render(request, 'todo_lists/task_list.html', {'tasks': tasks})

@login_required
def task_detail(request, pk):
    """View to display details of a specific task from the logged-in user's projects."""
    task = get_object_or_404(Task, pk=pk)
    
    # Check if the task belongs to the logged-in user's project
    if task.project and task.project.user != request.user:
        raise Http404("Task not found")
        
    return render(request, 'todo_lists/task_detail.html', {'task': task})

@login_required
def task_create(request):
    """View to create a new task for the logged-in user's projects."""
    # Get the user's projects for the dropdown
    projects = Project.objects.filter(user=request.user)
    
    if request.method == 'POST':
        # Process the form data
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        due_date_str = request.POST.get('due_date', '')
        project_id = request.POST.get('project', '')
        
        if title:
            # Handle the due date
            due_date = None
            if due_date_str:
                try:
                    # Parse the date string (adjust format as needed)
                    due_date = timezone.datetime.strptime(due_date_str, '%Y-%m-%dT%H:%M')
                    due_date = timezone.make_aware(due_date)
                except ValueError:
                    pass
            
            # Handle the project
            project = None
            if project_id:
                try:
                    # Ensure the project belongs to the user
                    project = Project.objects.get(id=project_id, user=request.user)
                except Project.DoesNotExist:
                    pass
            
            # Create the task
            task = Task.objects.create(
                title=title,
                description=description,
                due_date=due_date,
                project=project
            )
            return redirect('todo_lists:task_detail', pk=task.pk)
    
    return render(request, 'todo_lists/task_form.html', {'projects': projects})

@login_required
def task_update(request, pk):
    """View to update an existing task from the logged-in user's projects."""
    task = get_object_or_404(Task, pk=pk)
    
    # Check if the task belongs to the logged-in user's project
    if task.project and task.project.user != request.user:
        raise Http404("Task not found")
    
    # Get the user's projects for the dropdown
    projects = Project.objects.filter(user=request.user)
    
    if request.method == 'POST':
        # Process the form data
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        due_date_str = request.POST.get('due_date', '')
        project_id = request.POST.get('project', '')
        is_completed = request.POST.get('is_completed', '') == 'on'
        
        if title:
            # Handle the due date
            due_date = None
            if due_date_str:
                try:
                    # Parse the date string (adjust format as needed)
                    due_date = timezone.datetime.strptime(due_date_str, '%Y-%m-%dT%H:%M')
                    due_date = timezone.make_aware(due_date)
                except ValueError:
                    pass
            
            # Handle the project
            project = None
            if project_id:
                try:
                    # Ensure the project belongs to the user
                    project = Project.objects.get(id=project_id, user=request.user)
                except Project.DoesNotExist:
                    pass
            
            # Update the task
            task.title = title
            task.description = description
            task.due_date = due_date
            task.project = project
            task.is_completed = is_completed
            task.save()
            
            return redirect('todo_lists:task_detail', pk=task.pk)
    
    # Format the due date for the form
    due_date_formatted = ''
    if task.due_date:
        due_date_formatted = task.due_date.strftime('%Y-%m-%dT%H:%M')
    
    context = {
        'task': task,
        'projects': projects,
        'due_date': due_date_formatted
    }
    
    return render(request, 'todo_lists/task_form.html', context)

@login_required
def task_delete(request, pk):
    """View to delete a task from the logged-in user's projects."""
    task = get_object_or_404(Task, pk=pk)
    
    # Check if the task belongs to the logged-in user's project
    if task.project and task.project.user != request.user:
        raise Http404("Task not found")
    
    if request.method == 'POST':
        task.delete()
        return redirect('todo_lists:task_list')
    
    return render(request, 'todo_lists/task_confirm_delete.html', {'task': task})

@login_required
def task_toggle_completion(request, pk):
    """View to toggle the completion status of a task from the logged-in user's projects."""
    task = get_object_or_404(Task, pk=pk)
    
    # Check if the task belongs to the logged-in user's project
    if task.project and task.project.user != request.user:
        raise Http404("Task not found")
    
    # Toggle the completion status
    task.is_completed = not task.is_completed
    task.save()
    
    return redirect(request.META.get('HTTP_REFERER', reverse('todo_lists:task_list')))
