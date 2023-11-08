# serializers.py
from rest_framework import serializers
from .models import quiznames,QuizQuestion,QuizOption


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = quiznames
        fields = ('quiz_name', 'image','id')  # Define the fields you want to include in the API
class QuizNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = quiznames
        fields = '__all__'
class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = '__all__'


class QuizOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizOption
        fields = '__all__'