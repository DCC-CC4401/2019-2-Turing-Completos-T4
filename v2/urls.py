from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from turing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('landing_page/', views.landing_page, name='landing_page'),
    path('my_profile/', views.change_password, name='my_profile'),
    path('logout/', views.my_logout, name='logout'),
    path('upload_pic/', views.upload_pic, name='upload_pic')
]

urlpatterns += staticfiles_urlpatterns()
