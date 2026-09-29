import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "durgapuja.settings")
django.setup()

from django.contrib.auth.models import User

username = "Rahul kumar"
password = "Rahul2005&"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, "rahul@example.com", password)
    print(f"Superuser {username} created successfully!")
else:
    u = User.objects.get(username=username)
    u.set_password(password)
    u.save()
    print(f"Superuser {username} password updated successfully!")

