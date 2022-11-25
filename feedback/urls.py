from django.contrib import admin
from django.urls import path

from .views import DoneView, UpdateFeedbackView, FeedbackView, ListFeedBack

urlpatterns = [
    path('done', DoneView.as_view()),
    path('', FeedbackView.as_view()),  # as_view() специальный метод
    path('list', ListFeedBack.as_view()),
    path('<int:id_feedback>', UpdateFeedbackView.as_view()),
]
