from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "This is a custom command that does something useful"

    def handle(self, *args, **options):
        self.stdout.write("runnng my custom commands.")


