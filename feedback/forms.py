from django import forms


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=None, min_length=None, error_messages={
        'max_length': 'Слишком много символов',
        'min_length': 'Слишком мало символов',
        'required': 'Укажите хотя бы один символ',
    })
    surname = forms.CharField()
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}))
    rating = forms.IntegerField(label='Ratirng', max_value=10, min_value=1)
