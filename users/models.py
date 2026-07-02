from django.db import models
from django.contrib.auth.models import AbstractUser

import uuid

# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    email = models.EmailField(unique=True, db_index=True)
    