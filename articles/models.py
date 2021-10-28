from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse, reverse_lazy


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return f"{self.title} · {self.author.username}"

    def get_absolute_url(self):
        return reverse("article_details", args=[str(self.id)])


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} ⸱ {self.text}"

    def get_absolute_url(self):
        return reverse_lazy("article_details", args=[str(self.article.id)])
