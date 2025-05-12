from django.apps import AppConfig


class PractConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pract"

    def ready(self):
        import pract.signals
