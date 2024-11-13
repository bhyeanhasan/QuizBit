from django.contrib import admin
from .models import Exam, Enrollment, AnswerScript, Question, Option

# Register your models here.
admin.site.register(Exam)
admin.site.register(Enrollment)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(AnswerScript)
