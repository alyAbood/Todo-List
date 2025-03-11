# Task Manager

A simple task and project management application built with Django.

## Features

- Create, update, and delete tasks and projects
- Organize tasks within projects
- Track task completion status
- Set due dates for tasks
- Dashboard with task and project overview

## Deployment on Platform.sh

This application is configured for deployment on Platform.sh. To deploy:

1. Make sure you have the Platform.sh CLI installed and are logged in
2. Clone this repository
3. Run `platform create` to create a new project or `platform push` to push to an existing project

## Local Development

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Start the development server: `python manage.py runserver`

## License

MIT