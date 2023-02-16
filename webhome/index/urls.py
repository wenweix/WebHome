from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('page/<int:page>', page, name='page'),
    path('<int:a>/<str:func>/<int:b>', calc, name='calc'),
    path('req', req, name='req'),
    path('python', python, name='Python')
]
