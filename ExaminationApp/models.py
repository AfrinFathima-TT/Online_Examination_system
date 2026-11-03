from django.db import models

# Create your models here.

class QuestionDb(models.Model):
    question = models.CharField(max_length= 200)
    option_a = models.CharField(max_length= 100)
    option_b = models.CharField(max_length= 100)
    option_c = models.CharField(max_length= 100)
    option_d = models.CharField(max_length= 100)
    correct_answer = models.CharField(max_length=100)

class Submissionsdb(models.Model):
    student_name = models.CharField(max_length=100)
    student_email = models.CharField(max_length=200)
    question_id = models.IntegerField()
    selected_answer = models.CharField(max_length=100)
    submitted_date = models.DateTimeField(auto_now_add=True)