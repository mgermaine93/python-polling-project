from django.db import models


class Question(models.Model):
    # These are the question fields
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField('date published')

    # This displays the question text for questions
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # This foreign key in "question" links the choice to the question
    # .CASCADE means that if a question is deleted, all of its choices are deleted as well
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # This displays the choice text for choices
    def __str__(self):
        return self.choice_text
