from django.shortcuts import render
from .models import Walk
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
    return render(request, 'home.html')

def walks_index(request):
    walks = Walk.objects.all()
    return render(request, 'walks/index.html', {
        'walks': walks
    })

def walks_detail(request, walk_id):
    walk = Walk.objects.get(id=walk_id)
    return render(request, 'walks/detail.html', {
        'walk': walk
    })

class WalkCreate(CreateView):
    model = Walk
    fields = '__all__'

class WalkUpdate(UpdateView):
    model = Walk
    fields = ['miles', 'destination', 'hours']

class WalkDelete(DeleteView):
    model = Walk
    success_url = '/walks'