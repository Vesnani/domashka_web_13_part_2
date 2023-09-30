from django.urls import path
from quoteapp import views

app_name = 'quoteapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('create_author/', views.create_author, name='create_author'),
    path('create_tag/', views.create_tag, name='create_tag'),
    path('create_quote/', views.create_quote, name='create_quote'),
    path('authors/', views.authors_list, name='authors_list'),
    path('quotes/', views.quotes_list, name='quotes_list'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('tag/<int:pk>/', views.tag_detail, name='tag_detail'),
    path('quote/<int:pk>/', views.quote_detail, name='quote_detail'),
    path('tag/<int:pk>/', views.tag_detail, name='tag_detail'),
    path('quote/<int:pk>/', views.quote_detail, name='quote_detail'),
    path('authors_list/', views.authors_list, name='authors_list'),
    path('tags_list/', views.tags_list, name='tags_list'),
    path('quotes_list/', views.quotes_list, name='quotes_list'),
]