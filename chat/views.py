from django.shortcuts import render,get_object_or_404



from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import HttpResponse
# Create your views here.

def lobby(request):
    return render(request, 'chat/lobby.html')#




