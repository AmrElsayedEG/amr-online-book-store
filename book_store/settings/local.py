from .base import *
import os

DEBUG = os.environ.get("DEBUG")

SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = ['*']


DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE"),
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USERNAME"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOSTNAME"),
        "PORT": os.environ.get("DB_PORT"),
    }
}