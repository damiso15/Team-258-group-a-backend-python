import uuid
from employer.models import EmployerTable, AddressTable
from job_seeker.models import JobSeekerTable
from django.db import models

# Create your models here.


class JobTable(models.Model):
    job_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    employer_id = models.ForeignKey(EmployerTable, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255, db_index=True)
    job_description = models.TextField()
    # job_skills_tags =
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N/A', 'Rather not say'),
    )
    applicant_gender = models.CharField(max_length=50, choices=gender_choices, default='N/A')
    address = models.ForeignKey(AddressTable, on_delete=models.CASCADE)
    job_choices = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    job_open_for_application = models.CharField(max_length=50, choices=job_choices, default='Y')
    job_filled_choices = (
            ('Y', 'Yes'),
            ('N', 'No'),
        )
    job_filled = models.CharField(max_length=50, choices=job_filled_choices, default='Y')


class JobApplication(models.Model):
    job_id = models.ForeignKey(JobTable, on_delete=models.CASCADE)
    job_seeker_id = models.ForeignKey(JobSeekerTable, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    application_letter = models.TextField()
    application_submitted_choices = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    application_submitted = models.CharField(max_length=50, choices=application_submitted_choices, default='N')
    application_status_choices = (
        ('OP', 'Open'),
        ('UR', 'Under review'),
        ('R', 'Reviewed'),
        ('IS', 'Interview scheduled'),
        ('C', 'Closed'),
    )
    application_status = models.CharField(max_length=50, choices= application_status_choices, default='Y')
    # application_result = Pass / Fail
    # application_reviewed = True / False
