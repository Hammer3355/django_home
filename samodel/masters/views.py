from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string



def index(request):
    t = render_to_string('Путь к шаблону index.html')
    return HttpResponse(t)


def categories(request, cat_id):
    return HttpResponse(f'<h1>Категории</h1><p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Категории</h1><p>slug: {cat_slug}</p>')


def archive(request, year):
    if year > 2024:
        uri = reverse('cats', args=('music', ))
        return redirect(uri)

    return HttpResponse(f'<h1>Архив по годам</h1><p>year: {year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")