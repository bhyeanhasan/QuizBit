from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import ExamViewSet, EnrollmentViewSet, QuestionViewSet, OptionViewSet, AnswerScriptViewSet
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'exams', ExamViewSet, basename='exam')
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'options', OptionViewSet, basename='option')
router.register(r'answerscripts', AnswerScriptViewSet, basename='answerscript')

urlpatterns = [
    path('', include(router.urls)),
    path('home', views.index, name='index'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
