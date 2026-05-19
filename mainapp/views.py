from django.shortcuts import render, redirect
from .models import ThoughtPost

def home(request):
    
    if request.method == 'POST':
        content = request.POST.get('content')
        media = request.FILES.get('media')
        if content or media:
            ThoughtPost.objects.create(content=content, media=media)
            return redirect('home')
            
    posts = ThoughtPost.objects.all()
    return render(request, 'mainapp/3am_feed.html', {'posts': posts})

