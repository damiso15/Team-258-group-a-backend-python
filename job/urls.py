from django.urls import path
from .views import JobTableView, JobApplicationView


urlpatterns = [
    path('job/', JobTableView.as_view(), name='job'),
    path('application/', JobApplicationView.as_view(), name='application'),
]
