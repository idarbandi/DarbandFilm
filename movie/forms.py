from django import forms

from movie.models import Comment


class MovieCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('movie', 'user', 'created_time')
        labels = ({'body': 'ثبت نظر :'})
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control rounded-5',
                'id': 'textAreaExample',
                'rows': '4'
            })
        }
