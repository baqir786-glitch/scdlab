
from django.contrib import admin
from django.urls import path
from core import views  # Import your views module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),  # Root URL for the home page
    path('about/', views.about_view, name='about'),  # URL for about page
    path('services/', views.services_view, name='services'),  # URL for services page
    path('blog/', views.blog_view, name='blog'),  # URL for blog page
    path('signup/', views.user_signup, name='sign_up'),  # URL for user signup
    path('signin/', views.user_signin, name='sign_in'),
    path('welcome/', views.welcome_view, name='welcome'),  # Welcome page
   
        # URL for user signin
    
    
]
