from django.shortcuts import render
from django.http import Http404
from rest_framework import viewsets
from .serializers import BookSerializer, ChapterSerializer
from .models import Book, Chapter

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer

def BookList(request):
    return render(request, 'book/list.html', {'book_list': Book.objects.all()})

def ChapterList(request):
    return render(request, 'chapter/list.html', {'chapter_list': Chapter.objects.all()})

def BookDetail(request, book_id=0):
    try:
        book = Book.objects.get(id=book_id)
    except:
        raise Http404('Книга отсутствует!')
    return render(request, 'book/detail.html', {'book': book})

def ChapterDetail(request, chapter_id=0):
    try:
        chapter = Chapter.objects.get(id=chapter_id)
    except:
        raise Http404('Глава отсутствует!')
    return render(request, 'chapter/detail.html', {'chapter': chapter})