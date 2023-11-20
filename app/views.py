'''from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    title = request.POST.get('title', '')
    content = request.POST.get('content', '')

    context = {'title': title, 'content': content}
    return render(request, 'home.html', context)'''
from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')

        # Store the entered values in a list in the session
        entries = request.session.get('entries', [])
        entries.append({'title': title, 'content': content})
        request.session['entries'] = entries

    # Retrieve all entries from the session
    entries = request.session.get('entries', [])

    context = {'entries': entries}
    return render(request, 'home.html', context)

