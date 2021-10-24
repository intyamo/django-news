from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Article


class HomePageView(ListView):
    model = Article
    template_name = "home.html"
    context_object_name = "news_article_list"


class ArticleDetailsView(DetailView):
    model = Article
    template_name = "article_details.html"


class ArticleCreateView(CreateView):
    model = Article
    template_name = "article_create.html"
    fields = ["title", "author", "body"]


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "article_edit.html"
    fields = ["title", "body"]


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("home")
