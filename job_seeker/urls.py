from django.urls import path
from .views import JobSeekerView


urlpatterns = [
    path('jobseeker/', JobSeekerView.as_view(), name='jobseeker'),
]
