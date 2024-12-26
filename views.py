from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout ,get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from django.core.mail import send_mail
from .forms import UserSignUpForm, UserSignInForm
from .models import Blog, UserDetails  
import logging
from .models import SignInAttempt
# Ensure UserDetails is imported
def signup_success(request):
    return render(request, 'core/signup_success.html')
# Home Page View
def home_view(request):
    return render(request, 'core/home.html')
@login_required
def welcome_view(request):
    return render(request, 'core/welcome.html', {'username': request.user.username})
# About Page View
def about_view(request):
    return render(request, 'core/about.html')
# Services Page View
def services_view(request):
    return render(request, 'core/services.html')
# Blog Listing Page View
def blog_view(request):
    blogs = Blog.objects.all()
    return render(request, 'core/blog.html', {'blogs': blogs})
def blog_view(request):
    blogs = [
        {"id": 1, "title": "How to Boost Productivity", "description": "Learn the secrets of productivity to achieve more in less time."},
        {"id": 2, "title": "Top Web Design Trends", "description": "Explore the latest trends in web design for 2024."},
        {"id": 3, "title": "Effective Marketing Strategies", "description": "Discover the marketing strategies that work in the modern era."},
        {"id": 4, "title": "Why Cybersecurity Matters", "description": "Understand the importance of cybersecurity in the digital world."},
        {"id": 5, "title": "AI: The Future of Technology", "description": "Dive into the world of artificial intelligence and its potential."},
    ]
    return render(request, 'core/blog.html', {'blogs': blogs})

def services_view(request):
    services = [
        {"name": "Web Development", "description": "We build responsive and scalable websites tailored to your needs."},
        {"name": "Graphic Design", "description": "Our designs captivate audiences and leave a lasting impression."},
        {"name": "Digital Marketing", "description": "Boost your online presence with our innovative marketing strategies."},
        {"name": "SEO Optimization", "description": "Improve your search rankings and attract more traffic with our SEO services."},
        {"name": "IT Consulting", "description": "Get expert advice on IT solutions for your business challenges."},
    ]
    return render(request, 'core/services.html', {'services': services})
# Blog Detail Page View
def blog_detail_view(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'core/blog_detail.html', {'blog': blog})


User = get_user_model()
def user_signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            try:
                UserDetails.objects.create(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password1'],  # Hash if necessary
                )
                # Redirect to the success page
                return redirect('signup_success')
            except IntegrityError:
                form.add_error(None, 'A user with this username or email already exists.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserSignUpForm()
    return render(request, 'core/signup.html', {'form': form})


# User Logout View
@login_required
def user_logout(request):
    logout(request)
    return redirect('sign_in')  # Redirect to Sign In page after logout
# Get the custom logger
logger = logging.getLogger('sign_in_logger')


# Utility function to get client IP
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip











# def user_signin(request):
#     if request.method == 'POST':
#         form = UserSignInForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 # Log successful signin
#                 logger.info(f"Successful login for user: {username} (IP: {get_client_ip(request)})")
#                 login(request, user)
#                 return redirect('welcome')
#             else:
#                 # Log failed signin
#                 logger.warning(f"Failed login attempt for user: {username} (IP: {get_client_ip(request)})")
#                 messages.error(request, 'Invalid username or password.')
#         else:
#             # Log form validation errors
#             logger.error(f"Invalid signin form submission (IP: {get_client_ip(request)})")
#             messages.error(request, 'Please correct the errors below.')
#     else:
#         form = UserSignInForm()
#     return render(request, 'core/signin.html', {'form': form})

User = get_user_model()

def user_signin(request):
    if request.method == 'POST':
        form = UserSignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)  # Authenticate the user
            if user is not None:
                login(request, user)  # Log in the user
                return redirect('welcome')  # Redirect to the welcome page
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserSignInForm()
    return render(request, 'core/signin.html', {'form': form})














