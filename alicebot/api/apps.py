from django.apps import AppConfig
import threading
import asyncio

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'


