import os
from pathlib import Path

# For pytest-django, set the DJANGO_SETTINGS_MODULE to the test-specific settings.
os.environ['DJANGO_SETTINGS_MODULE'] = 'Task_Icecream_Project.settings_test'

# Path to your project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ":memory:",
    }
}
