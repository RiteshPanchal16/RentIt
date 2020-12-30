from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    path("index",views.index,name="index"),
    path("about",views.about,name="about"),
    path("home",views.home,name="home"),
    path("Login",views.Login,name="Login"),
    path("SignUp",views.SignUp,name="SignUp"),
    path("properties",views.properties,name="properties"),
    path("Services",views.Services,name="Services"),
    path("container",views.container,name="container"),
    
    
]