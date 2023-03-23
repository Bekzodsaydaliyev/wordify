from django.urls import path
from .views import index, article_detail, article_list, nav_views, category_view

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('list/', article_list, name='list'),
    path('detail/<int:pk>/', article_detail, name='detail'),
    path('nav/', nav_views, name='nav'),
    path('category/', category_view, name='category'),
]
