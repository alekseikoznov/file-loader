from django.urls import path

from files.views import FileListCreateView, FileListView

urlpatterns = [
    path('upload/', FileListCreateView.as_view(), name='file-upload'),
    path('files/', FileListView.as_view(), name='file-list'),
]
