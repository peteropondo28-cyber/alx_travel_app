import os
from dotenv import load_dotenv
load_dotenv() # Load environment variables from .env file

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- Basic Django Settings ---
SECRET_KEY = os.getenv('SECRET_KEY', 'your-insecure-default-secret-key-change-this-in-production')

DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['*'] # Change this in production

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party apps
    'rest_framework',
    'drf_spectacular',
    # My apps
    'books.apps.BooksConfig', # Assuming the app is named 'books'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    # ... (default template configuration)
]

# --- Database Configuration (MySQL) ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('MYSQL_DATABASE', 'mydjangodb'),
        'USER': os.getenv('MYSQL_USER', 'root'),
        'PASSWORD': os.getenv('MYSQL_PASSWORD', 'password'),
        'HOST': os.getenv('MYSQL_HOST', '127.0.0.1'),
        'PORT': os.getenv('MYSQL_PORT', '3306'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4', # Recommended charset for full Unicode support
        },
    }
}

# --- Django REST Framework Settings ---
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny', # Adjust permissions as needed
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# --- DRF Spectacular (Swagger/OpenAPI) Settings ---
SPECTACULAR_SETTINGS = {
    'TITLE': 'My Django API',
    'DESCRIPTION': 'A simple API for my project, documented with Swagger UI/Redoc.',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False, # Don't expose the schema endpoint in the UI itself
    'SWAGGER_UI_SETTINGS': {
        'deepLinking': True,
        'defaultModelsExpandDepth': 2,
        'defaultModelExpandDepth': 2,
    },
}

# ... (other default settings like AUTH_PASSWORD_VALIDATORS, STATIC_URL, etc.)
