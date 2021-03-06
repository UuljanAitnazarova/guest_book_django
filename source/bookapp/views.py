from django.shortcuts import render, redirect

from .models import Entry
from .forms import EntryForm


def index_view(request):
    entries = Entry.objects.filter(status='active').order_by('-created_at')
    return render(request, 'index.html', context={'entries':entries})
    

def entry_create_view(request):
    if request.method == 'GET':
        form = EntryForm()
        return render(request, 'entry_create.html', context={'form':form})
    elif request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            entry = Entry.objects.create(
                author = form.cleaned_data.get('author'),
                email = form.cleaned_data.get('email'),
                text = form.cleaned_data.get('text')
            )
            return redirect('index')
        return render(request, 'entry_create.html', context={'form':form})