from pathlib import Path
import os
import secrets

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("SECRET_KEY", default=secrets.token_hex())
DEBUG = os.getenv("DEBUG", default=False)

if DEBUG:
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = [os.getenv("SITE_DOMAIN")]

INSTALLED_APPS = [
    # * Downloaded Framewoks
    'waffle',
    'axes',
    'django_celery_beat',
    'django_celery_results',
    'rest_framework',
    'allauth',
    'allauth.account',
    'unfold',
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.inlines",
    "unfold.contrib.import_export",

    # * Django Stuff
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # * Apps
    'api.apps.ApiConfig',
    'landing.apps.LandingConfig',
    'tasks.apps.TasksConfig',
    'management.apps.ManagementConfig',
    'users.apps.UsersConfig',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
    'waffle.middleware.WaffleMiddleware',
    'axes.middleware.AxesMiddleware',
]
ROOT_URLCONF = 'core.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/"templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'core.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("POSTGRES_DB"),
        'HOST': os.getenv("POSTGRES_HOST"),
        'PASSWORD': os.getenv("POSTGRES_PASSWORD"),
        'USER': os.getenv("POSTGRES_USER"),
    }
}
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# * Security Configuration
X_FRAME_OPTIONS = 'SAMEORIGIN'
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = [
    f'http://{os.getenv("SITE_DOMAIN")}',
    f'https://{os.getenv("SITE_DOMAIN")}',
]
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
CSRF_TRUSTED_ORIGINS = [
    f'http://{os.getenv("SITE_DOMAIN")}',
    f'https://{os.getenv("SITE_DOMAIN")}',
]
if not DEBUG:
    SECURE_SSL_REDIRECT = True
AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesStandaloneBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
# * Allauth
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_NOTIFICATIONS = True
ACCOUNT_EMAIL_CONFIRMATION_HMAC = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_EMAIL_SUBJECT_PREFIX = os.getenv("EMAIL_SUBJECT_PREFIX")
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_PRESERVE_USERNAME_CASING = False
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_RATE_LIMITS = {"change_password": "5/d/user", "manage_email": "2/m/user", "reset_password": "5/d/ip,5/d/key",
                       "signup": "5/d/ip", "login": "10/d/ip", "login_failed": "3/5m/ip", "confirm_email": "1/5m/key"}
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ]
}

# * Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv("SMTP_SERVER")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")

# * AXES Configuration
AXES_ENABLED = True
AXES_FAILURE_LIMIT = 5
AXES_LOCK_OUT_AT_FAILURE = True
AXES_COOLOFF_TIME = 5
AXES_ONLY_ADMIN_SITE = False
AXES_ENABLE_ADMIN = True
AXES_VERBOSE = True
AXES_LOCKOUT_PARAMETERS = ["ip_address", ["username", "user_agent"]]
AXES_USERNAME_FORM_FIELD = 'login'

# * Celery settings
CELERY_BROKER_URL = 'redis://redisdb:6379/0'
CELERY_RESULT_BACKEND = "django-db"
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'
CELERY_IMPORTS = [
    'tasks.tasks',
]

# * Django-Unfold
UNFOLD = {
    "SITE_TITLE": os.getenv("SITE_TITLE"),
    "SITE_HEADER": os.getenv("SITE_TITLE"),
    "SITE_URL": "/",
    # "SITE_ICON": lambda request: static("icon.svg"),
    # "SITE_ICON": {
    #     "light": lambda request: static("images/logo-dark.png"),
    #     "dark": lambda request: static("images/logo-light.png"),
    # },
    # "SITE_LOGO": lambda request: static("logo.svg"),
    # "SITE_LOGO": {
    #     "light": lambda request: static("images/logo-dark.png"),
    #     "dark": lambda request: static("images/logo-light.png"),
    # },
    "SITE_SYMBOL": "speed",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "THEME": "dark",
    "COLORS": {
        "font": {
            "subtle-light": "107 114 128",
            "subtle-dark": "156 163 175",
            "default-light": "75 85 99",
            "default-dark": "209 213 219",
            "important-light": "17 24 39",
            "important-dark": "243 244 246",
        },
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
            "950": "59 7 100",
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
    }
}
