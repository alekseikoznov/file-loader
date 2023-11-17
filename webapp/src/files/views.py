from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response

from files.models import File
from files.serializers import FileSerializer
from files.tasks import process_file


class FileCreateView(CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        process_file.delay(serializer.instance.id)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )


class FileListView(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
