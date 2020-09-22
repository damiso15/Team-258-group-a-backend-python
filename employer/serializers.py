from rest_framework import serializers
from .models import EmployerTable, AddressTable


class EmployerSerializers(serializers.ModelSerializer):

    class Meta:
        model = EmployerTable
        fields = '__all__'


class AddressSerializers(serializers.ModelSerializer):

    class Meta:
        model = AddressTable
        fields = '__all__'
