from django.urls import path, include
from . import views

urlpatterns = [

    # BLOGAPP VIEWS
    path('', views.article_list, name='article_list'),
    path('create', views.create_article, name='create_article'),
    path('update/<int:article_id>/', views.update_article, name='update_article'),
    path('archive/<int:article_id>/', views.archive_article, name='archive_article'),
    path('delete/<int:article_id>/', views.delete_article, name='delete_article'),
    path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),
    path('signup/', views.signup, name = "signup"),
    path('login/', views.login, name = "login"),
    path('dashboard/', views.dashboard, name = "dashboard"),
]
