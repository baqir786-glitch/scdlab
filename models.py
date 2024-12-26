

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.
    """
    email = models.EmailField(unique=True, verbose_name="Email Address")

    # Specify related_name to avoid conflicts with auth.User relationships
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Avoid conflict with default User model
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to.',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Avoid conflict with default User model
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.username


class Blog(models.Model):
    """
    Model for blog posts.
    """
    title = models.CharField(max_length=255, verbose_name="Blog Title")
    content = models.TextField(verbose_name="Blog Content")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date Updated")

    def __str__(self):
        return self.title
from django.db import models

class UserDetails(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
    
class SignInAttempt(models.Model):
    username = models.CharField(max_length=150)
    ip_address = models.GenericIPAddressField()
    successful = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status = "Successful" if self.successful else "Failed"
        return f"{self.username} - {status} ({self.timestamp})"
