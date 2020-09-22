from django.shortcuts import render
from .serializers import EmployerSerializers, AddressSerializers
from .models import EmployerTable, AddressTable
from rest_framework import generics, mixins, status


# Create your views here.


class EmployerView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = EmployerSerializers
    queryset = EmployerTable.objects.all()

    def get(self, request):
        return self.list(request, status=status.HTTP_200_OK)

    def post(self, request):
        return self.create(request, status=status.HTTP_201_CREATED)

    def put(self, request):
        return self.update(request, status=status.HTTP_200_OK)

    def delete(self, request):
        return self.destroy(request, status=status.HTTP_204_NO_CONTENT)


class AddressView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                         mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = AddressSerializers
    queryset = AddressTable.objects.all()

    def get(self, request):
        return self.list(request, status=status.HTTP_200_OK)

    def post(self, request):
        return self.create(request, status=status.HTTP_201_CREATED)

    def put(self, request):
        return self.update(request, status=status.HTTP_200_OK)

    def delete(self, request):
        return self.destroy(request, status=status.HTTP_204_NO_CONTENT)
