from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=10, min_length=2, error_messages={
        'max_length': 'Too many symbols',
        'min_length': 'Too little symbols',
        'required': 'Indicate at minimum one symbol',
    })
    surname = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}))
    rating = forms.IntegerField(label='Ratirng', max_value=10, min_value=1)
