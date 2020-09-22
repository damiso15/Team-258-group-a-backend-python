import uuid
from django.db import models

# Create your models here.


class JobSeekerTable(models.Model):
    job_seeker_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    # job_seeker_organisation_type =
