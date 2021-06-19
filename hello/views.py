from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(response):
    return HttpResponse('<!doctype html>\
                        <h1>Добро пожаловать<h1>\
                        <a href="/hello/about">О нас</a>')


# self.assertRegex(content, r'<!doctype\s+html>', msg="Должен быть задан doctype")
# test_html_in_about
def about(response):
    return HttpResponse('<!doctype html>\
                        <html>\
                            <head> <title>Резюме</title> </head>\
                            <body>\
                                <h1>О нас</h1>\
                                <h3>Я - Павел</h3>\
                                <p>Мне 20 лет</p>\
                                <p>Я учусь в университете шаг</p>\
                                <a href="/hello/">На главную</a>\
                            </body>\
                        </html>')
