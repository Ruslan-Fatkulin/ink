from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all/', views.all, name='all'),
    path('application/', views.application, name='application'),
    path('detail/<int:pk>', views.detail, name='detail')
]
