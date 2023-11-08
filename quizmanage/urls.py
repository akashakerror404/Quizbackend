from django.urls import path
from .views import QuizList
from .views import QuizQuestionsOptions

urlpatterns = [
    path('quiz_all/', QuizList.as_view(), name='quiz_all'),
    path('quiz_question/<int:quiz_id>/', QuizQuestionsOptions.as_view(), name='quiz-questions-options'),

]
