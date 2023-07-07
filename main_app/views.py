from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def walks_index(request):
    return render(request, 'walks/index.html', {
        'walks': walks
    })