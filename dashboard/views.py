from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def HomeView(request):
     return render(request, 'home.html')

@login_required
def AddProductView(request):
     return render(request, 'adicionar.html')