from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm


# Create your views here.
#  7.5
def index(request):
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm()
        print(form.cleaned_data)
        return HttpResponseRedirect('/done')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback.html',
                  {'form': form})  # во всех других случаях мы не передаем ошибку


def done(request):
    return render(request, 'feedback/done.html')
