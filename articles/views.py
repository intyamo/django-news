from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Article, Comment


class HomePageView(ListView):
    model = Article
    template_name = "home.html"
    context_object_name = "news_article_list"


class ArticleDetailsView(DetailView):
    model = Article
    template_name = "article_details.html"


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_create.html"
    fields = ["title", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    template_name = "article_edit.html"
    fields = ["title", "body"]

    def test_func(self):
        return self.get_object().author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        return self.get_object().author == self.request.user


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "comment_create.html"
    fields = ["text"]

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['article'] = get_object_or_404(Article, id=self.kwargs["article_pk"])
    #     return context

    def article(self):
        """
        Returns article to which new comment relates.
        Meant to be used within create new comment template context.
        """
        return get_object_or_404(Article, id=self.kwargs.get("article_pk"))

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article_id = self.kwargs.get("article_pk")
        return super().form_valid(form)
