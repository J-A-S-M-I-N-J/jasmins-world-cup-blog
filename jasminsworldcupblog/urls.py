from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('about', views.About.as_view(), name='about'),
    path('donate', views.Donate.as_view(), name='donate'),
    path('bookmark/<slug:slug>/', views.Bookmark.as_view(), name='bookmark'),
    path('add', views.add_item, name='add'),
    path('edit/<item_id>', views.edit_item, name = 'edit'),
    path('toggle/<item_id>', views.toggle_item, name = 'toggle'),
    path('delete/<item_id>', views.delete_item, name='delete'),
]