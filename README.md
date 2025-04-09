
# Link Shortener Web Application

## Overview

I created a simple link shortener web application using Django, which allows users to shorten URLs, manage their shortened links, and view the remaining time until their shortened links expire. This project helps users keep track of their URLs and provides an easy way to manage them. The inspiration for this project came from a desire to have a simple and effective tool for shortening URLs, managing them, and sharing them.

This web application includes the following features:

- User registration and login using Django's built-in authentication system.
- A URL shortening feature where users can shorten their links.
- Ability to view all shortened links and see when they will expire.
- A delete feature for removing links that are no longer needed.
- Display of remaining days/hours/minutes before link expiration.

## Distinctiveness and Complexity

This project stands out because:

- It includes Django's built-in authentication system, ensuring that only authenticated users can create, view, and delete their shortened links.
- Expiration logic for shortened links ensures that links become inactive after a set period, preventing link abuse.
- The project utilizes Django's ORM for managing URL shortening, expiration, and user data.
- Includes a clean, responsive design built using HTML, CSS, and JavaScript, with a focus on usability and simplicity.

I used Django's built-in features for user authentication, URL handling, and database management to build this project.

## Files and Directories

- linkshortener: main project directory.
    - settings.py: contains Django settings, including configurations for the database and email.
    - urls.py: defines the project's URL patterns.
    - wsgi.py: entry point for WSGI servers.
    - asgi.py: entry point for ASGI servers.
- shortener: name of the application directory.
    - migrations: contains database migrations.
    - static: contains static files (CSS, JS).
    - templates: contains HTML templates for the user interface.
    - admin.py: registers models to be used in the Django admin.
    - models.py: contains the models (tables) for managing links and expiration logic.
    - urls.py: defines URLs specific to the 'shortener' app.
    - views.py: contains the views for handling user requests and displaying links.
- db.sqlite3: the default database used by Django to store URL and user data.

## Models

This project uses two models:

1. **User**: An extension of Django's AbstractUser class, handling user authentication and management.
2. **ShortenedURL**: Stores the original URL, shortened code, expiration time, and the user who created it.

## How to Run the Application

1. Install Python if not already done so.
2. Create a virtual environment inside the project directory:
    - `python -m venv venv`
3. Activate the virtual environment:
    - On Windows: `venv\Scripts activate`
    - On macOS/Linux: `source venv/bin/activate`
4. Install Django:
    - `pip install django`
5. Install the required packages:
    - `pip install -r requirements.txt`
6. Apply the migrations:
    - `python manage.py migrate`
7. Create a superuser to access the Django admin:
    - `python manage.py createsuperuser`
8. Run the server:
    - `python manage.py runserver`
9. Visit the application in your browser:
    - Go to `http://localhost:8000/`

## Features

- **User Registration and Login**: Users can create an account, log in, and manage their shortened links.
- **Shorten URLs**: Users can input a long URL and generate a short version that they can share.
- **Expiration Time**: Each shortened URL has an expiration time set to 5 days by default, after which the link becomes inactive.
- **Link Management**: Users can view all their shortened links, check the expiration time, and delete links they no longer need.

