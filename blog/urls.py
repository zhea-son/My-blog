from django.urls import path
from .views import Login, index
from .views import bloglist, post_detail, Login, signup

urlpatterns = [
    path('',index, name='index'),
    path('bloglist/', bloglist, name='bloglist'),
    path('postdetail/<int:id>/', post_detail , name='post_detail'),
    path('LogIN/', Login.as_view(), name='login'),
    path('SignUp/', signup.as_view(), name='signup'),
]


