from django.urls import path
from .views import index
from .views import bloglist, post_detail

urlpatterns = [
    path('',index, name='index'),
    path('bloglist/', bloglist, name='bloglist'),
    path('postdetail/<int:id>/', post_detail , name='post_detail')
]

