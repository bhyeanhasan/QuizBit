from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('App_ExamManager.urls')),
    path('admin/', admin.site.urls),
]
