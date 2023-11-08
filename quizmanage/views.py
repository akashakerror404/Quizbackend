from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response  # Add this import
from .models import quiznames, QuizQuestion, QuizOption


# Create your views here.

from .models import quiznames
from .serializers import *

class QuizList(APIView):
    def get(self, request):
        quizzes = quiznames.objects.all()
        serializer = QuizSerializer(quizzes, many=True)
        print(serializer.data)
        return Response(serializer.data)


class QuizQuestionsOptions(APIView):
    def get(self, request, quiz_id):
        try:
            # Get the quiz based on the provided quiz_id
            quiz = quiznames.objects.get(pk=quiz_id)

            # Get the questions related to the quiz
            questions = QuizQuestion.objects.filter(quiz_name=quiz)

            question_and_options = []

            for question in questions:
                # Get the options for each question
                options = QuizOption.objects.filter(question=question)
                
                # Create a dictionary for the question and its options
                question_data = {
                    "question_text": question.question_text,
                    "question_id": question.id,

                    "options": [
                        {
                            "option_text": option.option_text,
                            "is_correct": option.is_correct
                        }
                        for option in options
                    ]
                }
                
                question_and_options.append(question_data)

            # Serialize the data if using Django REST framework serializers
            quiz_data = QuizNamesSerializer(quiz).data

            # Return the serialized data
            return Response({
                "quiz": quiz_data,
                "questions_and_options": question_and_options,
            })

        except quiznames.DoesNotExist:
            return Response(
                {"error": "Quiz not found"},
                status=status.HTTP_404_NOT_FOUND
            )

      