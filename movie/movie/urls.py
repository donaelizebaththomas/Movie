"""
URL configuration for movie project.

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
#  to display the image in the website
from django.conf import settings
from django.conf.urls.static import static

from app import views

app_name='app'
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.home,name='home'),
    path('',views.HomeView.as_view(),name="home"),
    # path('viewmovie/<int:d>',views.viewmovie,name='viewmovie'),
    path('viewmovie/<int:pk>',views.Details.as_view(),name='viewmovie'),
    # path('edit/<int:d>/',views.edit,name='edit'),
    path('edit/<int:pk>',views.Update.as_view(),name='edit'),
    # path('add',views.add,name='add'),
    path('add',views.Addmovie.as_view(),name='add'),
    # path('delete/<int:d>/',views.delete,name='delete'),
    path('delete/<int:pk>',views.Delete.as_view(),name='delete'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

