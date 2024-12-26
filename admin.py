from django.contrib import admin
from .models import UserDetails
from .models import SignInAttempt

@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')

@admin.register(SignInAttempt)
class SignInAttemptAdmin(admin.ModelAdmin):
    list_display = ('username', 'ip_address', 'successful', 'timestamp')
    list_filter = ('successful', 'timestamp')
    search_fields = ('username', 'ip_address')
