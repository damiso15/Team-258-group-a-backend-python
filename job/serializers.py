from rest_framework import serializers
from .models import JobTable, JobApplication


class JobTableSerializers(serializers.ModelSerializer):

    class Meta:
        model = JobTable
        fields = '__all__'


class JobApplicationSerializers(serializers.ModelSerializer):

    class Meta:
        model = JobApplication
        fields = '__all__'
