from django import forms

from news.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']

        widgets = {
            'comment_text': forms.Textarea(
                attrs={'class': 'form-control', 'rows': '5', 'cols': '30', 'placeholder': 'Comment'})
        }
