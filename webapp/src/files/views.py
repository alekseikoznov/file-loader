from rest_framework import generics

from files.models import File
from files.serializers import FileSerializer
from files.tasks import process_file


class FileListCreateView(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        process_file.delay(instance.id)


class FileListView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
