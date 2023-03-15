from rest_framework import viewsets, filters

from textbook.models import BookTag, Textbook, Syllabus, Course
from textbook.permissions import IsAdminUserOrReadOnly
from textbook.serializers import SyllabusSerializer, TextbookSerializer, CourseSerializer, BookTagSerializer


# Create your views here.
class BookTagViewSet(viewsets.ModelViewSet):
    queryset = BookTag.objects.all()
    serializer_class = BookTagSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class TextbookViewSet(viewsets.ModelViewSet):
    queryset = Textbook.objects.all()
    serializer_class = TextbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = '__all__'

    def perform_create(self, serializer):
        serializer.save(uploader=self.request.user)


class SyllabusViewSet(viewsets.ModelViewSet):
    queryset = Syllabus.objects.all()
    serializer_class = SyllabusSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = '__all__'

    def perform_create(self, serializer):
        serializer.save(uploader=self.request.user)