from http.client import responses
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import F
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from .serializers import ExamSerializer, QuestionSerializer, OptionSerializer, AnswerScriptSerializer, \
    EnrollmentSerializer
from .models import Exam, Question, Option, AnswerScript, Enrollment
from django.contrib.auth.decorators import login_required, user_passes_test
from rest_framework.permissions import IsAdminUser, IsAuthenticated


def index(request):
    return HttpResponse("Welcome To QuizBit")


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsAdminUser]

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def questions(self, request, pk=None):
        exam = self.get_object()
        questions = Question.objects.filter(exam=exam)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAdminUser]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAdminUser]


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = [IsAdminUser]


class AnswerScriptViewSet(viewsets.ModelViewSet):
    queryset = AnswerScript.objects.all()
    serializer_class = AnswerScriptSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data

        enrollment_id = data.get('enrollment')
        question_id = data.get('question')
        selected_option_id = data.get('selected_option')

        enrollment = get_object_or_404(Enrollment, id=enrollment_id)
        question = get_object_or_404(Question, id=question_id)
        selected_option = get_object_or_404(Option, id=selected_option_id, question=question)

        exam = enrollment.exam

        if exam.start_time + timedelta(minutes=exam.duration) < timezone.now():
            return JsonResponse({"message": "Exam has ended."}, status=400)
        if timezone.now() < exam.start_time:
            return JsonResponse({"message": "Exam has not started yet."}, status=400)

        is_correct = selected_option.is_correct

        pass_marks = exam.passing_marks
        score = enrollment.score

        if is_correct:
            score += question.marks
            if score >= pass_marks:
                enrollment.status = 'passed'
            enrollment.score = score
            enrollment.save()

        answer_script = AnswerScript.objects.create(
            enrollment=enrollment,
            question=question,
            selected_option=selected_option
        )
        serializer = self.get_serializer(answer_script)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_question_set(request, id):
    exam = get_object_or_404(Exam, id=id)

    questions = Question.objects.filter(exam=exam)

    if not questions:
        return HttpResponse(f"No questions found for exam {exam.title}", status=404)

    question_set = []
    for question in questions:
        options = Option.objects.filter(question=question)

        question_set.append({
            'id': question.id,
            'text': question.text,
            'options': [
                {'id': option.id, 'text': option.text} for option in options
            ]
        })

    return JsonResponse({'exam': exam.title, 'questions': question_set}, safe=False)


@api_view(['GET'])
def get_practice_history(request, username):
    user = get_object_or_404(User, username=username)
    practice_history = Enrollment.objects.filter(student=user)

    if not practice_history.exists():
        return JsonResponse({"message": f"No practice history found for user '{username}'."}, status=404)

    history_data = []
    for entry in practice_history:
        history_data.append({
            "exam_id": entry.exam.id,
            "exam_title": entry.exam.title,
            "score": entry.score,
            "status": entry.status,

        })

    return JsonResponse({"username": username, "practice_history": history_data}, safe=False)
