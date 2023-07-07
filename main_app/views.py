from django.shortcuts import render

# Temporary walks model, until Class Based View is created
walks = [
    {'date': '2023-07-06', 'miles': 3, 'destination': 'Store', 'hours': 1.5},
    {'date': '2023-07-07', 'miles': 4, 'destination': 'Supermarket', 'hours': 2}
]



# Create your views here.
def home(request):
    return render(request, 'home.html')

def walks_index(request):
    return render(request, 'walks/index.html', {
        'walks': walks
    })