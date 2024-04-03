import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.reusable import TimeStamps


class User(TimeStamps, AbstractUser):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(unique=True, max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=100)
    otp = models.IntegerField(null=True, blank=True)
    last_login = models.DateTimeField(null=True, blank=True)
    otp_generated_at = models.DateTimeField(null=True, blank=True)
    failed_login_attempts = models.IntegerField(default=0)
    last_failed_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_locked = models.BooleanField(default=False)
    dob = models.DateField()

    REQUIRED_FIELDS = ["email", "password"]



