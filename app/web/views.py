from django.shortcuts import render, redirect, reverse
from app.api.models import News
from app.web.forms import NewsForm


def home(request):
    return render(request, 'pages/list.html', {})


def add_news(request):
    mi_form = NewsForm()
    # Validamos el formulario
    if request.method == 'POST':
        mi_form = NewsForm(request.POST)
        # Muestro los errores
        if mi_form.is_valid():
            # Guardo
            mi_new_news = News()
            mi_new_news.title = mi_form.cleaned_data.get('title')
            mi_new_news.url = mi_form.cleaned_data.get('url')
            mi_new_news.save()
            # Redirecciono a Home
            return redirect(reverse('list'))
    return render(request, 'pages/add-news.html', {
        'news_form': mi_form
    })