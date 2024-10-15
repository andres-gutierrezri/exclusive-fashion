from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path("", views.home, name="home"),
    path("inicio/", views.inicio, name="inicio"),
    path('login/', views.login, name='login'),
    path('crear_cuenta/', views.crear_cuenta, name='crear_cuenta'),
    path("productos/", views.productos, name="productos"),
    path("ofertas/", views.ofertas, name="ofertas"),
    path("contacto/", views.contacto, name="contacto"),
    path("hombres/", views.hombres, name="hombres"),
    path("mujeres/", views.mujeres, name="mujeres"),
    path("infantil/", views.infantil, name="infantil"),
    path("nosotros/", views.nosotros, name="nosotros"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
