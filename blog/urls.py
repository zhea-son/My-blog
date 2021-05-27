from django.urls import path
from .views import index
from .views import bloglist

urlpatterns = [
    path('',index, name='index'),
    path('bloglist/', bloglist, name='bloglist'),
]

