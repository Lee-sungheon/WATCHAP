from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('hello/', views.hello, name="hello"),
    path('', views.movies_list_create),
    path('<int:movie_pk>/list_create_movie_comment/', views.list_create_movie_comment),
    path('delete_movie_comment/<int:comment_pk>/', views.delete_movie_comment),
    path('delete_review_comment/<int:review_comment_pk>/', views.delete_review_comment),
    path('<int:movie_pk>/like_movie/', views.like_movie),
    path('<int:movie_pk>/select_movie/', views.select_movie),
    path('<int:movie_pk>/list_create_movie_review/', views.list_create_movie_review),
    path('<int:review_pk>/list_create_review_comment/', views.list_create_review_comment),
    path('update_delete_movie_review/<int:review_pk>/', views.update_delete_movie_review),
    path('<int:review_pk>/like_review/', views.like_review),
]
