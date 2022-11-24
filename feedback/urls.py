from django.contrib import admin
from django.urls import path

from .views import done, UpdateFeedbackView, FeedbackView

urlpatterns = [
    path('done', done),
    path('', FeedbackView.as_view()),  # as_view() специальный метод
    path('<int:id_feedback>', UpdateFeedbackView.as_view()),
]
