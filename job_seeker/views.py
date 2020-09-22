from django.shortcuts import render
from .serializers import JobSeekerSerializers
from .models import JobSeekerTable
from rest_framework import generics, mixins, status


# Create your views here.


class JobSeekerView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = JobSeekerSerializers
    queryset = JobSeekerTable.objects.all()

    def get(self, request):
        return self.list(request, status=status.HTTP_200_OK)

    def post(self, request):
        return self.create(request, status=status.HTTP_201_CREATED)

    def put(self, request):
        return self.update(request, status=status.HTTP_200_OK)

    def delete(self, request):
        return self.destroy(request, status=status.HTTP_204_NO_CONTENT)
