# Django Todo List Application with Tailwind CSS

![Todo App Screenshot](screenshot.png) 

## Overview

A modern, responsive todo list application built with Django (MVT architecture) and styled with Tailwind CSS. The app features user authentication, CRUD operations for tasks, and a clean dark-themed interface with yellow accents.

## Features

- **User Authentication**: Sign up, login, and logout functionality
- **Todo Management**:
  - Create new tasks with titles and descriptions
  - Mark tasks as pending/completed
  - Edit existing tasks
  - Delete tasks
- **Responsive Design**: Works on all device sizes
- **Modern UI**: Dark theme with yellow accents (bg-gray-900 and #FFE31A)
- **Status Tracking**: Visual indication of task status (pending/completed)

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, Tailwind CSS
- **Database**: SQLite (default Django database)

## Installation

### Prerequisites

- Python 3.8+
- Node.js (for Tailwind CSS)
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/django-todo.git
   cd django-todo
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Tailwind CSS**:
   ```bash
   python manage.py tailwind install
   ```

5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional)**:
   ```bash
   python manage.py createsuperuser
   ```

## Running the Application

1. **Start the development server**:
   ```bash
   python manage.py tailwind start
   python manage.py runserver
   ```

2. **Access the application**:
   - Open your browser and go to `http://localhost:8000`
   - For admin access: `http://localhost:8000/admin`

## Project Structure

```
django-todo/
├── todo/                      # Main app directory
│   ├── migrations/            # Database migrations
│   ├── templates/             # HTML templates
│   │   ├── todo/              # Todo-related templates
│   │   └── registration/      # Authentication templates
│   ├── __init__.py
│   ├── admin.py               # Admin configuration
│   ├── apps.py
│   ├── forms.py               # Form definitions
│   ├── models.py              # Database models
│   ├── tests.py
│   ├── urls.py                # App URL routing
│   └── views.py               # View functions
├── todo_project/              # Project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL routing
│   └── wsgi.py
├── theme/                     # Tailwind CSS theme
├── db.sqlite3                 # Database file
├── manage.py                  # Django management script
└── requirements.txt           # Python dependencies
```

## Customization

### Colors

The application uses the following color scheme by default:
- Background: `bg-gray-900` (#111827)
- Accent: `yellow-500` (#FFE31A)

To change the colors:
1. Edit the Tailwind configuration in `theme/static_src/tailwind.config.js`
2. Update the color classes in the HTML templates

### Adding Features

Some potential enhancements:
- Due dates for tasks
- Task categories/tags
- Search functionality
- Drag-and-drop task reordering

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Screenshots


## Support

For any issues or questions, please open an issue on the GitHub repository.