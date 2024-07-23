from django.shortcuts import get_object_or_404, render
from .models import YourModel

def detail_view(request, pk):
    obj = get_object_or_404(YourModel, pk=pk)
    context = {'object': obj}
    return render(request, 'your_app/detail.html', context)

