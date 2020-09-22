import uuid
from django.db import models

# Create your models here.


class AddressTable(models.Model):
    main_complex = models.IntegerField()
    unit_number = models.IntegerField()
    sub_complex = models.IntegerField()
    street_number = models.IntegerField()
    street_name = models.CharField(max_length=255)
    neighbourhood = models.CharField(max_length=255)
    suburb = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    postal_code = models.IntegerField()
    country = models.IntegerField(max_length=255)
    GPS_coordinates = models.IntegerField()


class EmployerTable(models.Model):
    employer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    employer_name = models.CharField(max_length=255)
