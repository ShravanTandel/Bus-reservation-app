"""dbmsP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from dbmsA import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('searchbusesfrom<str:s>to<str:d>on<str:d1>', views.search, name = 'search'),
    path('<str:s>to<str:d>on<str:d1>by<str:orderby>', views.orderby, name = 'orderby'),
    path('<int:id>', views.seat, name = 'seat'),
    path('register', views.register, name='register'),
    path('registercomapny', views.addcompany, name='addcompany'),
    path('addbus', views.addbus, name='addbus'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('<str:seatno>and<int:busno>and<int:seatid>', views.enterdetails, name='enterdetails'),
    path('rating/<int:passid>/<int:busid>', views.rating, name='rating'),
    path('books', views.books, name='books'),
    path('update<int:pk>', views.updatep, name='update'),
    path('cancel<int:id>', views.cancel, name='cancel'),
    path('deletecompany<int:id>', views.deletecompany, name='deletecompany'),
    path('deletebus<int:id>', views.deletebus, name='deletebus'),
    path('deletepassenger<int:id>', views.deletepassenger, name='deletepassenger'),
    path('viewbooks', views.viewbooks, name='viewbooks'),
    path('cancelbooks<int:id>', views.cancelbooks, name='cancelbooks'),
]
