from django.urls import path
from . import views

urlpatterns = [

    # The home page
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),

]
