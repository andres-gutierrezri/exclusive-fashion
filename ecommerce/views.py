from django.shortcuts import render


def home(request):
    return render(request, "ecommerce/home.html")


def login(request):
    return render(request, "ecommerce/home.html")


def crear_cuenta(request):
    return render(request, "ecommerce/home.html")


def inicio(request):
    return render(request, "ecommerce/tienda.html")


def productos(request):
    return render(request, "ecommerce/home.html")


def ofertas(request):
    return render(request, "ecommerce/home.html")


def contacto(request):
    return render(request, "ecommerce/home.html")


def hombres(request):
    return render(request, "ecommerce/home.html")


def mujeres(request):
    return render(request, "ecommerce/home.html")


def infantil(request):
    return render(request, "ecommerce/home.html")


def nosotros(request):
    return render(request, "ecommerce/home.html")
