from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=50)
    message = models.TextField()

# version: '3'
# services:
#   db:
#     image: postgres:11
#     volumes:
#     - db-data:/var/lib/postgres/data
#   django_proj:
#     build: .
#     command: >
#         bash -c "python manage.py migrate &&
#                  python manage.py runserver 0.0.0.0:7777"
#     volumes:
#     - ./django_data:/var/lib/django/data
#     ports:
#       - "7777:7777"
#     depends_on:
#       - db
# volumes:
#   db-data: