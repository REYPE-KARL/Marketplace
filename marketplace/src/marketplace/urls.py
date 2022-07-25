"""marketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from accounts.views import signup, logout_user, login_user, profile_user
from contacts.views import contact
from marketplace import settings


urlpatterns = [
    #admin's page
    path('admin/', admin.site.urls),
    #store's page
    path('', include('store.urls')),

    #account's page
    path('signup/', signup, name="signup"),
    path('logout/', logout_user, name="logout"),
    path('login/', login_user, name="login"),
    path('profile/<str:slug>/', profile_user, name="profile"),

    #contact's page
    path('contact/', contact, name="contact"),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
