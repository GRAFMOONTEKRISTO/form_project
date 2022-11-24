from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback

from django.views import View


# Create your views here.

class FeedbackView(View):
    def get(self, request):  # отвечает за get запросы
        form = FeedbackForm()
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request):  # отвечает за post запросы
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect('/done')
        return render(request, 'feedback/feedback.html', context={'form': form})


class UpdateFeedbackView(View):
    def get(self, request, id_feedback):  # отвечает за get запросы
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request, id_feedback):  # отвечает за post запросы
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForm(instance=feed)
        if request.method == 'POST':
            form = FeedbackForm(request.POST, instance=feed)
            if form.is_valid():
                print(form.cleaned_data)
                form.save()
                return HttpResponseRedirect('/done')
        return render(request, 'feedback/feedback.html', context={'form': form})

def done(request):
    return render(request, 'feedback/done.html')

# 7.5 + addendum 7.9 with cut a codes
# def index(request):
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect('/done')
#     else:
#         form = FeedbackForm()
#     return render(request, 'feedback/feedback.html', context={'form': form})


# Кад ниже позволяет нам делать изменения , не добавляя новые записи в БД, в существующие поля
# def update_feedback(request, id_feedback):
#     feed = Feedback.objects.get(id=id_feedback)
#     if request.method == 'POST':
#         form = FeedbackForm(request.POST, instance=feed)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect('/done')
#     else:
#         form = FeedbackForm(instance=feed)
#
#     return render(request, 'feedback/feedback.html', context={'form': form})



