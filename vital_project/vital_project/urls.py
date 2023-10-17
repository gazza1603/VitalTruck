from django.contrib import admin
from django.urls import path, include
from vital_app.views import login_view  # Import the login view

urlpatterns = [
    path('', login_view, name='home'),  # Set the login view as the home page
    path('admin/', admin.site.urls),
    path('', include('vital_app.urls')),

]