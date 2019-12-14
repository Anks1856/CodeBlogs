
from django.urls import path
from . import views

urlpatterns = [
    path('',views.bloghome,name = 'bloghome'),
    path("<str:slag>", views.blogpost,name = 'blogpost'),
]