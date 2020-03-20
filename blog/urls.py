from django.urls import path
from . import views
from .views import PostListView, PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView,GenreListView,AuthorListView,SuscribeView,Genre1PostListView,Genre2PostListView,Genre3PostListView,Genre4PostListView,Genre5PostListView


urlpatterns=[
    path('blog-home/',PostListView.as_view(),name='blog-home'),
    path('suscribe/1',Genre1PostListView.as_view(),name='genre-1'),
    path('suscribe/2',Genre2PostListView.as_view(),name='genre-2'),
    path('suscribe/3',Genre3PostListView.as_view(),name='genre-3'),
    path('suscribe/4',Genre4PostListView.as_view(),name='genre-4'),
    path('suscribe/5',Genre5PostListView.as_view(),name='genre-5'),
    path('suscribe/success/',views.success,name='success'),
    path('',views.intro,name='intro'),
    path('author_int',AuthorListView.as_view(),name='author-int'),
    path('join/',views.join_team,name='join_team'),
    path('genre/',views.genre_list,name='genre-list'),
	path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('about/',views.about,name='blog-about'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
	path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
    path('suscribe/',SuscribeView.as_view(),name='suscribe'),
    path('random/',views.random,name='random'),
]
    
                
