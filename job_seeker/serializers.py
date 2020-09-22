from rest_framework import serializers
from .models import JobSeekerTable


class JobSeekerSerializers(serializers.ModelSerializer):

    class Meta:
        model = JobSeekerTable
        fields = '__all__'
