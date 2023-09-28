from django.urls import path, include
from django.shortcuts import redirect
from django.contrib import admin

urlpatterns = [
     path('', include('brightBoostApp.urls')),  # Include your app's URLs
    path('admin/', admin.site.urls),
    # ... other URL patterns for your project ...
]
