from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_default_superuser(sender, **kwargs):
    User = get_user_model()
    if not User.objects.filter(is_superuser=True).exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@amr.com',
            password='admin'
        )
        print("Superuser created: admin / admin")
