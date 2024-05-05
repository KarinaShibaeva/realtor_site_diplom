from django import forms
from django.utils.translation import gettext_lazy as _
from comment.models import Comment


class CommentForm(forms.Form):
    author = forms.CharField(widget=forms.TextInput(attrs={"class":"myfield", 'placeholder': 'Имя'}), label=_(u'Имя'))
    email=forms.CharField(widget=forms.TextInput(attrs={"class":"myfield", 'placeholder': 'Email'}))
    phone=forms.CharField(widget=forms.TextInput(attrs={"class":"myfield", 'placeholder': 'Телефон'}), label=_(u'Телефон'))
    text = forms.CharField(widget=forms.TextInput(attrs={"class":"myfield", 'placeholder': 'Ваш вопрос'}), label=_(u'Ваш вопрос'))
    class Meta:
        model = Comment
        exclude = ('date_of_create','published','post')
