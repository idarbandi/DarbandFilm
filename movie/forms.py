from django import forms


class MovieCommentForm(forms.Form):
    Comment = forms.CharField(max_length=1200)
