from django.contrib import admin
from django.urls import include, path
from django.test import TestCase
from django import forms
#from . import views
from WoodWork.views import *

urlpatterns = [

    path("", Index.as_view(), name="index"),
    path("madera/", MaderaListView.as_view(), name="madera-list"),
    path("cliente/", ClienteListView.as_view(), name="cliente-list"),
    path("empleado/", EmpleadoListView.as_view(), name="empleado-list"),
    path("presupuesto/", PresupuestoListView.as_view(), name="presupuesto-list"),
    path("articulo/", ArticuloLisView.as_view(), name="articulo-list"),

    path("madera/<int:pk>/", MaderaDetailView.as_view(), name="madera-detail"),
    path("cliente/<int:pk>/", ClienteDetailView.as_view(), name="cliente-detail"),
    path("empleado/<int:pk>/", EmpleadoDetailView.as_view(), name="empleado-detail"),
    path("presupuesto/<int:pk>/", PresupuestoDetailView.as_view(), name="presupuesto-detail"),
    path("articulo/<int:pk>/", ArticuloDetailView.as_view(), name="articulo-detail"),

    path("madera/add/", MaderaCreateView.as_view(), name="madera-add"),
    path("madera/<int:pk>/update/", MaderaUpdateView.as_view(), name="madera-update"),
    path("madera/<int:pk>/delete/", MaderaDeleteView.as_view(), name="madera-delete"),

    path("cliente/add/", ClienteCreateView.as_view(), name="cliente-add"),
    path("cliente/<int:pk>/update/", ClienteUpdateView.as_view(), name="cliente-update"),
    path("cliente/<int:pk>/delete/", ClienteDeleteView.as_view(), name="cliente-delete"),

    path("empleado/add/", EmpleadoCreateView.as_view(), name="empleado-add"),
    path("empleado/<int:pk>/update/", EmpleadoUpdateView.as_view(), name="empleado-update"),
    path("empleado/<int:pk>/delete/", EmpleadoDeleteView.as_view(), name="empleado-delete"),

    path("presupuesto/add/", PresupuestoCreateView.as_view(), name="presupuesto-add"),
    path("presupuesto/<int:pk>/update/", PresupuestoUpdateView.as_view(), name="presupuesto-update"),
    path("presupuesto/<int:pk>/delete/", PresupuestoDeleteView.as_view(), name="presupuesto-delete"),

    path("articulo/add/", ArticuloCreateView.as_view(), name="articulo-add"),
    path("articulo/<int:pk>/update/", ArticuloUpdateView.as_view(), name="articulo-update"),
    path("articulo/<int:pk>/delete/", ArticuloDeleteView.as_view(), name="articulo-delete"),

    path("search/", SearchResultsView.as_view(), name="search_results"),
    path("search/<int:pk>", MaderaDetailView.as_view(), name="search_results_madera"),

    #path('login/', LoginView.as_view(), name='registration-login'),
    #path("accounts/", include("django.contrib.auth.urls")),
    #path("accounts/register/", View.register_request, name="register"),
    #path("", TemplateView.as_view(template_name="home.html"), name="home"),

    path('presupuesto/<int:pk>/generar_pre/', generar_pdf_presupuesto, name='generar_pre'),
    path('presupuesto/<int:pk>/generar_fac/', generar_pdf_factura, name='generar_pre'),

    path('openid/', include('django_openid_auth.urls')),
    path('accounts/', include('allauth.urls')),
]

