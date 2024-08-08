from django.shortcuts import render


def login(request):
    response = render(request, 'dashboard.html',)
    response.status_code = 200
    return response


def handler404(request, exception):
    response = render(request, '404.html',)
    response.status_code = 404
    return response


def handler500(request):
    response = render(request, '404.html',)
    response.status_code = 500
    return response
