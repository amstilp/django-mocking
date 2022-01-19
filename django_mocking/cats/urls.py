from django.urls import path

from . import views

urlpatterns = [
    path('randomcat', views.RandomCat.as_view(), name='randomcat'),
 ]
