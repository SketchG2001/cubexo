from django.apps import AppConfig


class ObappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'obapp'

    def ready(self):
        import obapp.signals
