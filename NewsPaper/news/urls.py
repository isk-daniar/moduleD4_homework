from django.urls import path
from .views import NewsListView, NewsDetailView, SearchView, NewsCreateView, NewsUpdateView, NewsDeleteView

urlpatterns = [
    path('', NewsListView.as_view(), name='post_list'),
    path('<int:pk>', NewsDetailView.as_view(), name='post'),
    path('search/', SearchView.as_view(), name='news_search'),
    path('add/', NewsCreateView.as_view(), name='news_create'),
    path('<int:pk>/edit/', NewsUpdateView.as_view(), name='news_edit'),
    path('<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    
]