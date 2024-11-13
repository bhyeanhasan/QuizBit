from django.contrib.auth.models import User
from django.db import models
from App_QuestionManager.models import Question, Option


class Exam(models.Model):
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exams')
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    total_marks = models.PositiveIntegerField()
    passing_marks = models.PositiveIntegerField()
    start_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    status = models.CharField(max_length=10, choices=[('passed', 'Passed'), ('failed', 'Failed')], default='failed')

    def __str__(self):
        return f"{self.student.username} - {self.exam.title} Attempt"


class AnswerScript(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.enrollment.student.username}'s answer for {self.question.text}"
