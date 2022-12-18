from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('about', views.About.as_view(), name='about'),
    path('donate', views.Donate.as_view(), name='donate'),
    path('bookmark/<slug:slug>/', views.bookmark.as_view(), name='bookmark'),
    path('add', views.add_item, name='add'),
    path('edit/<slug:slug>/', views.edit_item, name='edit'),
    path('toggle/<slug:slug>/', views.toggle_item, name='toggle'),
    path('deletecheck/<slug:slug>/', views.delete_item_view, name='deletecheck'),
    path('delete/<slug:slug>/', views.delete_post, name='delete_post'),
    path('profile', views.profile, name='profile'),
    path('postlist', views.PostList.as_view(), name='PostList'),
]