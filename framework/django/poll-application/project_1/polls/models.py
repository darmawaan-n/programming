from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(name='question', max_length=255)
    pub_date = models.DateTimeField(name='date published')

class Choice(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    choice_text = models.CharField(name='choice', max_length=255)
    votes = models.IntegerField(name='vote', default=0)