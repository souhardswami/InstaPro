"""instapro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include

from . import views

urlpatterns = [
    

    path('follower/',views.Follower.as_view()),
    path('following/',views.Following.as_view()),
    path('post/',views.Post.as_view()),
    path('userAuth/',views.userAuth.as_view()),
    path('userImage/',views.userImage.as_view()),
    path('search/',views.Search.as_view()),
    path('comments/',views.Comments.as_view()),
    path('likes/',views.Likes.as_view()),
    path('registor/',views.Registor.as_view()),
    path('editprofile/<int:pk>',views.EditProfile.as_view()),
    path('newpost/',views.NewPost.as_view()),
    path('newcomment/',views.NewComment.as_view()),
    
    
]