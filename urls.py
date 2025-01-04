from django.urls import path
from Home import views

urlpatterns = [
    path('', views.index, name='home'),  # Homepage
    path('/submission', views.submission, name='submission'),
]
