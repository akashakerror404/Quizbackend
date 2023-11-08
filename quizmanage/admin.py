from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
admin.site.register(quiznames)
admin.site.register(QuizQuestion)
admin.site.register(QuizOption)