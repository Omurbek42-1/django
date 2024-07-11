from django.shortcuts import render
from django.http import HttResponse


def index(reguest):
    return  HttResponse("<h4>Проверка работы</h4>")


def about(reguest):
    return HttResponse("<h4>Страница про нас</h4>")