from django.db import models
from App_ExamManager.models import Exam


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    text = models.TextField()
    marks = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Question {self.id} for {self.exam.title}"


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Option {self.text} for {self.question.id}"
