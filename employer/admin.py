from django.contrib import admin
from .models import EmployerTable, AddressTable

# Register your models here.


admin.site.register(EmployerTable)
admin.site.register(AddressTable)
