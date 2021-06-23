from django.shortcuts import render


def home(request):
    return render(request, 'pages/list.html', {})


def add_news(request):
    return render(request, 'pages/add-news.html', {})