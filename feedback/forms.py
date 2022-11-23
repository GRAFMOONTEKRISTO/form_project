from django import forms
from .models import Feedback


# class FeedbackForm(forms.Form):
#     name = forms.CharField(max_length=10, min_length=2, error_messages={
#         'max_length': 'Too many symbols',
#         'min_length': 'Too little symbols',
#         'required': 'Indicate at minimum one symbol',
#     })
#     surname = forms.CharField()
#     feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}))
#     rating = forms.IntegerField(label='Ratirng', max_value=10, min_value=1)

# оба класса несут одинаковую логуку в разработке, но нижний вариант короче и удобнее - урок 7.9ddd
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        labels = {
            'name': 'Name',
            'surname': 'Surname',
            'feedback': 'Feedback',
            'rating': 'Rating',
        }

        error_messages = {
            'name': {
                'max_length': 'Too many symbols',
                'min_length': 'Too little symbols',
                'required': 'Indicate at minimum one symbol',
            },
            'surname': {
                'max_length': 'Too many symbols',
                'min_length': 'Too little symbols',
                'required': 'Indicate at minimum one symbol',
            }
        }
