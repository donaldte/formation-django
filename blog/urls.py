from django.urls import path
from blog.views import ArticleCreateView, ArticleDeleteView, ArticleDetailView, ArticleListView, ArticleUpdateView

app_name='blog'
urlpatterns = [
     path('',ArticleListView.as_view(), name='article-list'),
     path('<int:pk>/detail', ArticleDetailView.as_view(), name='article-detail'),
     path('<int:pk>/update', ArticleUpdateView.as_view(), name='article-update'),
     path('create', ArticleCreateView.as_view(), name='article-create'),
     path('<int:pk>/delete', ArticleDeleteView.as_view(), name='article-delete'),

]
