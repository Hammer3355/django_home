from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

data_db = [
    {'id': 1, 'title': 'Андженина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True},
    {'id': 4, 'title': 'Евгений Сахаров', 'content': 'Биография Евгения Сахарова', 'is_published': True},
]


def index(request):
    # t = render_to_string('masters/index.html')
    # return HttpResponse(t)
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db
    }
    return render(request, 'masters/index.html', context=data)


def about(request):
    return render(request, 'masters/about.html', {'title': 'О сайте'})


def categories(request, cat_id):
    return HttpResponse(f'<h1>Категории</h1><p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Категории</h1><p>slug: {cat_slug}</p>')


def archive(request, year):
    if year > 2024:
        uri = reverse('cats', args=('music',))
        return redirect(uri)

    return HttpResponse(f'<h1>Архив по годам</h1><p>year: {year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
