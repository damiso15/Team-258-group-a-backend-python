from django.urls import path
from .views import EmployerView, AddressView


urlpatterns = [
    path('employer/', EmployerView.as_view(), name='employer'),
    path('address/', AddressView.as_view(), name='address'),
]
