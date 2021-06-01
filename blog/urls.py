from django.urls import path
from .views import deleteblog, index
from .views import bloglist, post_detail, Login, signup, addblog, deleteblog

urlpatterns = [
    path('',index, name='index'),
    path('bloglist/', bloglist, name='bloglist'),
    path('postdetail/<int:id>/', post_detail , name='post_detail'),
    path('LogIN/', Login.as_view(), name='login'),
    path('SignUp/', signup.as_view(), name='signup'),
    path('AddBlog/', addblog.as_view(), name='addblog'),
    path('deleteblog/<int:id>/', deleteblog, name='deleteblog'),
    # path('editblog/<int:id>', editblog.as_view(), name='editblog'),
]


