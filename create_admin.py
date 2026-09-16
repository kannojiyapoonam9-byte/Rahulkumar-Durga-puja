import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "durgapuja.settings")
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('Raju', 'admin@example.com', 'Raju1219')
    print("Superuser 'admin' created successfully!")
else:
    print("Superuser 'admin' already exists.")


# # Purana admin
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')

# # Naya admin (aise add kar sakte hain)
if not User.objects.filter(username='Rahul').exists():
    User.objects.create_superuser('Raju', 'rohit@example.com', 'Rahul2005@')