from django.shortcuts import render
from .models import play

# Create your views here.
def playpage(request):
    #play = play.object.all().order_by('date')
    return render(request , 'playpage/playpage.html')
