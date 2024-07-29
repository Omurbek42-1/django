from django.shortcuts import render, redirect
from .forms import PostForm

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Перенаправление на страницу со списком постов или другую подходящую страницу
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
