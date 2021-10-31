from django.urls import path

from .views import (
    HomePageView,
    ArticleDetailsView,
    ArticleCreateView,
    ArticleUpdateView,
    ArticleDeleteView,
    CommentCreateView,
    CommentCreate_Alt_View
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("article/new", ArticleCreateView.as_view(), name="article_create"),
    path("article/<int:pk>/", ArticleDetailsView.as_view(), name="article_details"),
    path("article/<int:pk>/edit", ArticleUpdateView.as_view(), name="article_edit"),
    path("article/<int:pk>/delete", ArticleDeleteView.as_view(), name="article_delete"),
    path("article/<int:article_pk>/comment", CommentCreateView.as_view(), name="comment_create"),
    path("article/comment/", CommentCreate_Alt_View.as_view(), name="comment_create_alt"),
]
