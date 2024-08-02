# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Book
from django.core.serializers import serialize
import json

@csrf_exempt
@require_http_methods(["GET", "POST"])
def book_list(request):
    if request.method == "GET":
        books = Book.objects.all()
        books_json = serialize('json', books)
        return JsonResponse(books_json, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        book = Book.objects.create(**data)
        return JsonResponse({"id": book.id}, status=201)

@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return JsonResponse({"error": "Book not found"}, status=404)

    if request.method == "GET":
        book_json = serialize('json', [book])
        return JsonResponse(book_json, safe=False)
    elif request.method == "PUT":
        data = json.loads(request.body)
        for attr, value in data.items():
            setattr(book, attr, value)
        book.save()
        return JsonResponse({"id": book.id})
    elif request.method == "DELETE":
        book.delete()
        return JsonResponse({}, status=204)


# views.py
from django.http import JsonResponse
from django.views import View
from django.core.serializers import serialize
from .models import Book
import json

class BookList(View):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        books_json = serialize('json', books)
        return JsonResponse(books_json, safe=False)

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        book = Book.objects.create(**data)
        return JsonResponse({"id": book.id}, status=201)

class BookDetail(View):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        book = self.get_object(pk)
        if not book:
            return JsonResponse({"error": "Book not found"}, status=404)
        book_json = serialize('json', [book])
        return JsonResponse(book_json, safe=False)

    def put(self, request, pk, *args, **kwargs):
        book = self.get_object(pk)
        if not book:
            return JsonResponse({"error": "Book not found"}, status=404)
        data = json.loads(request.body)
        for attr, value in data.items():
            setattr(book, attr, value)
        book.save()
        return JsonResponse({"id": book.id})

    def delete(self, request, pk, *args, **kwargs):
        book = self.get_object(pk)
        if not book:
            return JsonResponse({"error": "Book not found"}, status=404)
        book.delete()
        return JsonResponse({}, status=204)

