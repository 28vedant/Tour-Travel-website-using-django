"""
URL configuration for Tourtravel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Tourtravelapp import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('india/', views.india, name='india'),
    path('europe/', views.europe, name='europe'),
    path('thailand/', views.thailand, name='thailand'),
    path('malaysia/', views.malaysia, name='malaysia'),
    path('searchpakages/', views.searchpakages, name='searchpakages'),
    path('showcart/', views.showcart, name='showcart'),
    path('addtocart/<int:pid>', views.addtocart, name='addtocart'),
    path("updateqty/<int:qv>/<int:pid>", views.updateqty, name="updateqty"),
    path('payment/' , views.payment ,name='payment'),
    path('showbooking/', views.showbooking, name='showbooking'),
    path('userdetails/', views.userdetails, name='userdetails'),
    path('addpakages/', views.addpakages, name='addpakages'),
    path('showpakage/', views.showpakage, name='showpakage'),
    path('updatepakage/', views.updatepakage, name='updatepakage'),




]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
