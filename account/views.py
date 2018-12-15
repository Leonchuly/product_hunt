from django.shortcuts import render

# Create your views here.

def loginup(request):
    return render(request,'loginup.html')