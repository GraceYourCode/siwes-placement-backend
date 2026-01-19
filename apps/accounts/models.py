import uuid
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email_address, password=None, **extra_fields):
        if not email_address:
            raise ValueError("Users must have a email address")
        email_address = self.normalize_email(email_address)
        user = self.model(email_address=email_address, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email_address, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email_address, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        app_label = "apps"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email_address = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    other_names = models.CharField(max_length=30, null=True, blank=True)
    role = models.CharField(
        max_length=20,
        choices=[
            ("student", "Student"),
            ("institution", "Institution Admin"),
            ("supervisor", "Supervisor"),
            ("mentor", "Company Mentor"),
        ],
    )
    created_at = models.DateField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email_address"

    objects = UserManager()

    def __str__(self):
        return self.email_address
