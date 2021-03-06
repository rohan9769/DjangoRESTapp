"""myRESTapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import article_list,student_list,article_detail,ArticleAPIView,ArticleDetailsAPIView,StudentDetailsAPIView,GenericAPIView

urlpatterns = [
    path('article/', article_list),
    path('student/', student_list),
    path('detail/<int:pk>/', article_detail),
    path('articleAPIView/',ArticleAPIView.as_view()), #as_view() since ArticleAPIView is a classbased apiview
    path('articledetailsAPIView/<int:id>/',ArticleDetailsAPIView.as_view()),
    path('studentdetailsAPIView/',StudentDetailsAPIView.as_view()),
    path('generic/article/',GenericAPIView.as_view())
]
