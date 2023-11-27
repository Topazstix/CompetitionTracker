import os
from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ("DJANGO_SUPERUSER_USERNAME")
email = os.environ("DJANGO_SUPERUSER_EMAIL")
password = os.environ("DJANGO_SUPERUSER_PASSWORD")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print(f"Superuser {username} created.")
else:
    print(f"Superuser {username} already exists.")