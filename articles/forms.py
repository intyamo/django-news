from django import forms
from django_select2 import forms as s2forms

from .models import Comment


class ArticleWidget(s2forms.ModelSelect2Widget):
    search_fields = (
        "title__icontains",
        "author__username__icontains",
    )


class CommentForm(forms.ModelForm, s2forms.ModelSelect2Mixin):
    class Meta:
        model = Comment
        fields = ("article", "text")

        # in the code below we initialize widget with select2 specific html attributes:
        # https://select2.org/configuration/data-attributes
        # if you don't need any, you can specify just a widget class
        # "article": ArticleWidget,
        # you can add any other html attributes too, if needed
        widgets = {
            "article": ArticleWidget(
                attrs={"data-placeholder": "-- select article --",
                       "data-ajax--delay": 250,
                       }),
        }
