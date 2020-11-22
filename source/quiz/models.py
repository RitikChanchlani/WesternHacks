# abandoned django code. For improvement use later
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE

class Quiz (models.Model):
    name = models.Charfield(Max_length=100)
    description = models.CharField(max_length = 70) 
    image = models.ImageField()
    short_label = models.SlugField(black = True)
    roll_out = models.BooleanField(default = False)
    timestamp = models.DateTimeField(add = True)

    class Meta:
        ordering = ['timestamp',]
        name_plural = "Quizzes"
    
    def _str_(self):
        return self.name

class Questions(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete = models.CASCADE)
    label = models.CharField(auto_now_add = True)
    order = models.IntegerField(default = 0)
    
    def _str_(self):
        return self.label
class Answer (models.Model):
    question = models.ForeignKey(Questions, on_delete = models.CASCADE):
    label = models.CharField(max_length=100)
    is_correct = models.BooleanField(default = False)

    def _str_(self):
        return self.label


class QuizTaker(models.odel):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete= models.CASCADE)
    score = models.IntegerField(default = 0)
    completed = models.BooleanField(default=False)
    date_finished = models.DateTimeField
    timestamp = models.DateTimeField(add = True)

    def _str_(self):
        return self.username


class UsersAnswers (models.Model):
    quiz_taker = models.ForeignKey9QuizTaker, on_delete = models.CASCASE)
    question = models.ForeignKey(Questions, on_delete = models.CASCADE)
    question = models.ForeignKey(Answer, on_delete = models.CASCADE)

    def _str_(self):
        return self.username




    
