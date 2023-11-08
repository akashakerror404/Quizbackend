
# Create your models here.
from django.db import models

class quiznames(models.Model):
    quiz_name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='quiznimage', null=True, blank=True)

    
    def __str__(self):
        return self.quiz_name


class QuizQuestion(models.Model):
    quiz_name = models.ForeignKey(quiznames, on_delete=models.CASCADE)

    question_text = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.question_text

class QuizOption(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=700)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.option_text
