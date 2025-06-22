# Social Media App

A modern social media platform built with Django and Bootstrap, featuring user authentication, profile management, and interactive post functionality.

## Features

- User authentication (register, login, logout)
- Email confirmation for new registrations
- User profiles with profile pictures
- Create, read, update, and delete posts
- Like and unlike posts
- Comment on posts
- View posts by specific users
- Real-time chat messaging
- Private conversations between users
- Unread message notifications
- Responsive design with Bootstrap
- PostgreSQL database support
- Crispy Forms integration for beautiful form styling

## Installation

1. Clone the repository:
```
git clone <repository-url>
cd social_media_app
```

2. Create a virtual environment and activate it:
```
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```
pip install -r requirements.txt
```

4. Configure your PostgreSQL database settings in `socialmedia/settings.py`

5. Configure email settings in `socialmedia/settings.py`:
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-specific-password'
```

6. Apply migrations:
```
python manage.py makemigrations
python manage.py migrate
```

7. Create a superuser (admin):
```
python manage.py createsuperuser
```

8. Run the development server:
```
python manage.py runserver
```

9. Open your browser and navigate to `http://127.0.0.1:8000/`

## Usage

1. Register a new account or login with an existing account
2. Create a new post by clicking on "New Post" in the navigation bar
3. View all posts on the home page
4. Click on a post title to view the full post and its comments
5. Like posts by clicking the heart icon
6. Comment on posts by using the comment form on the post detail page
7. Update your profile by clicking on "Profile" in the navigation bar
8. View posts by a specific user by clicking on their username

## Technologies Used

- Django
- Bootstrap 5
- PostgreSQL (database)
- Crispy Forms with Bootstrap 5 integration
- Pillow (for image processing)
- psycopg2-binary (PostgreSQL adapter)
- AJAX for real-time chat updates

## License

This project is licensed under the MIT License - see the LICENSE file for details.
