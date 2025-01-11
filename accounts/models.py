from django.contrib.auth.models import User
from django.db.models import CASCADE, Model, OneToOneField, TextField


class Profile(Model):
    # OneToOne field insemna ca fiecare user este asociat cu un singur profil si vice-versa
    user = OneToOneField(User, on_delete=CASCADE)
