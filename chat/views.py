from django.shortcuts import render


def index(request):
    return render(request, 'chat/chat_main.html', {})

def signin(request):
    return render(request, 'chat/signin.html', {})

def signup(request):
    return render(request, 'chat/signup.html', {})

def reservation(request):
    return render(request, 'chat/reservation.html', {})

def houseKeeping(request):
    return render(request, 'chat/houseKeeping.html', {})

def fbConcierge(request):
    return render(request, 'chat/fbConcierge.html', {})