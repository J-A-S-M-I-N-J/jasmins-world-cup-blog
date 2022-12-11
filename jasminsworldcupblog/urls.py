from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('/about', views.About.as_view(), name='about'),
    path('/donate', views.Donate.as_view(), name='donate'),
]
