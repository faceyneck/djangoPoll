from django.db import models
from django.utils import timezone
import datetime 
# Create your models here.
"""
In our poll app, we’ll create two models: Question and Choice. A Question has a question and a publication date. A Choice has two fields: the text of the choice and a vote tally. Each Choice is associated with a Question.
"""

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # question_text, pub_date above are called "Field instances"
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # question, choice_text, and votes above are called "Field instances" in Django parlance.
    def __str__(self):
        return self.choice_text
    # adding in a custom method to our model. (AKA not imported in but defined here)
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)