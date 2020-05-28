from django.shortcuts import render


def login(request):
    return render(request, 'login.html')


def callback(request):
    return render(request, 'callback.html')


def get_token(request):
    return render(request, 'get_token.html')
