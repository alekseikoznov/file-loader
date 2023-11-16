from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import File


class FileUploadTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.test_file = open('files/file.txt', 'rb')

    def test_file_upload(self):
        url = reverse('file-upload')
        data = {'file': self.test_file}
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(File.objects.count(), 1)
        self.assertEqual(File.objects.get().processed, False)

    def test_file_list(self):
        # Добавьте запрос на получение списка файлов перед тестом
        self.test_file_upload()

        url = reverse('file-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Изменим утверждение, чтобы проверить, что длина больше 0
        self.assertGreaterEqual(len(response.data), 1)
