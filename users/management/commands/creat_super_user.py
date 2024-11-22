from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email="kavyabass51@gmail.com",
            first_name="Vasya",
            last_name="Korobov",
            is_staff=True,
            is_superuser=True,
        )
        user.is_active = True
        user.set_password("qwerasdf1234")
        user.save()
