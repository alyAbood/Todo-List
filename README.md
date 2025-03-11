# Task Manager

A modern task and project management application built with Django and Bootstrap 5. This web application follows Material Design principles and provides an intuitive interface for managing tasks and projects.

## Features

- **User Authentication**: Secure login, registration, and account management
- **User-Specific Data**: Each user has their own projects and tasks for data isolation
- **Project Management**: Create, update, and delete projects to organize your work
- **Task Management**: Create tasks with descriptions, due dates, and project assignment
- **Task Status Tracking**: Mark tasks as complete/incomplete with visual indicators
- **Dashboard**: Overview of projects and pending tasks with statistics
- **Responsive Design**: Works on mobile, tablet, and desktop devices
- **Material Design**: Modern UI with Material icons and consistent design patterns

## UI Features

- **Sticky Footer**: Footer always stays at the bottom of the viewport
- **Properly Aligned Icons**: Material Design icons aligned correctly with text in buttons
- **Consistent Spacing**: Proper spacing between UI elements following Material Design guidelines
- **Responsive Layouts**: Adaptive layouts that work across different screen sizes
- **Accessible Design**: High contrast text and proper semantic HTML structure

## Technology Stack

- **Backend**: Django 5.1
- **Database**: PostgreSQL (Production), SQLite (Development)
- **Frontend**: Bootstrap 5, CSS3, HTML5, JavaScript
- **Icons**: Material Design Icons
- **Deployment**: Platform.sh

## Deployment on Platform.sh

This application is deployed on Platform.sh. To deploy:

1. Make sure you have the Platform.sh CLI installed and are logged in
2. Clone this repository
3. Run `platform create` to create a new project or `platform push` to push to an existing project

### Platform.sh Configuration

- Python 3.11 runtime
- PostgreSQL 15 database
- Automated deploy hooks for database migrations
- Static file handling with proper caching

## Local Development

1. Clone the repository
2. Create a virtual environment: `python -m venv tl_env`
3. Activate the virtual environment: `source tl_env/bin/activate` (Linux/Mac) or `tl_env\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Create a superuser: `python manage.py createsuperuser`
7. Start the development server: `python manage.py runserver`
8. Access the application at http://localhost:8000

## Project Structure

- `todo_lists/`: Main application with models, views, and templates
- `accounts/`: User authentication and profile management
- `tl_project/`: Project settings and configuration
- `.platform/`: Platform.sh deployment configuration
- `static/`: Static files (CSS, JS, images)

## License

MIT

## Live Demo

The application is accessible at: https://main-bvxea6i-7ie3lri6flzt6.us-3.platformsh.site/