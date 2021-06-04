from django.urls import path
from .views import deleteblog, EditBlog, index
from .views import BlogList, post_detail, Login, Signup, AddBlog, deleteblog

urlpatterns = [
    path('',index, name='index'),
    path('bloglist/', BlogList.as_view(), name='bloglist'),
    path('postdetail/<int:id>/', post_detail , name='post_detail'),
    path('LogIN/', Login.as_view(), name='login'),
    path('SignUp/', Signup.as_view(), name='signup'),
    path('AddBlog/', AddBlog.as_view(), name='addblog'),
    path('deleteblog/<int:id>/', deleteblog, name='deleteblog'),
    path('editblog/<int:id>', EditBlog.as_view(), name='editblog'),
]


