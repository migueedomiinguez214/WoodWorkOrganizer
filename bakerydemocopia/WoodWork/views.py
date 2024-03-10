from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic import ListView, DetailView
from WoodWork.models import Madera,Cliente,Empleado,Presupuesto, Articulo
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views import View
from django.shortcuts import  redirect
from .form import NewUserForm
from django.contrib import messages
from decimal import Decimal, ROUND_HALF_UP
from django.db.models import Q 
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from reportlab.pdfgen import canvas


# ListViews
class Index(TemplateView):
    template_name = 'home.html'

class MaderaListView(ListView):
    model = Madera

    def get_queryset(self):
        queryset = Madera.objects.all()

        # Filtrar por tipo
        tipos_filter = self.request.GET.get('tipos')
        queryset = queryset.filter(tipos=tipos_filter)

        return queryset

class ClienteListView(ListView):
    model = Cliente

class EmpleadoListView(ListView):
    model = Empleado



class PresupuestoListView(ListView):
    model = Presupuesto

class ArticuloLisView(ListView):
    model = Articulo

# DetailsViews
class MaderaDetailView(DetailView):
    context_object_name = "Madera"
    queryset = Madera.objects.all()

class ClienteDetailView(DetailView):
    context_object_name = "Cliente"
    queryset = Cliente.objects.all()

class EmpleadoDetailView(DetailView):
    context_object_name = "Empleado"
    queryset = Empleado.objects.all()

class PresupuestoDetailView(DetailView):
    context_object_name = "Empleado"
    queryset = Presupuesto.objects.all()

class ArticuloDetailView(DetailView):
    context_object_name = "Articulo"
    queryset = Articulo.objects.all()

#MaderaCUPViews

class MaderaCreateView(CreateView):
    model = Madera
    fields = '__all__'


class MaderaUpdateView(UpdateView):
    model = Madera
    fields = '__all__'
    

class MaderaDeleteView(DeleteView):
    model = Madera
    success_url = reverse_lazy("madera-list")

#ClienteCUPViews

class ClienteCreateView(CreateView):
    model = Cliente
    fields = '__all__'


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = '__all__'
    

class ClienteDeleteView(DeleteView):
    model = Cliente
    success_url = reverse_lazy("cliente-list")

#EmpleadoCUPViews

class EmpleadoCreateView(CreateView):
    model = Empleado
    fields = '__all__'

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    fields = '__all__'
    

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    success_url = reverse_lazy("empleado-list")

#PresupuestoCUPViews

class PresupuestoCreateView(CreateView):
    model = Presupuesto
    fields = ["dni_cliente", "num", "articulos", "precio_final"]


class PresupuestoUpdateView(UpdateView):
    model = Presupuesto
    fields = ["dni_cliente", "num", "articulos", "precio_final"]
    

class PresupuestoDeleteView(DeleteView):
    model = Presupuesto
    success_url = reverse_lazy("presupuesto-list")

#ArticuloCUPViews

class ArticuloCreateView(CreateView):
    model = Articulo
    fields = '__all__'

class ArticuloUpdateView(UpdateView):
    model = Articulo
    fields = '__all__'
    

class ArticuloDeleteView(DeleteView):
    model = Articulo
    success_url = reverse_lazy("articulo-list")

#logins

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})

def sesion_iniciada(request):
    return render(request, template_name="/registration/sesion-iniciada")

#search
class SearchResultsView(View):
    template_name = 'search_results.html'

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        all_results = {}

        if query:
            # Realiza la búsqueda en Madera
            madera_results = Madera.objects.filter(tipos__icontains=query)
            all_results['madera_results'] = madera_results

            # Realiza la búsqueda en Cliente
            cliente_results = Cliente.objects.filter(nombre__icontains=query)
            all_results['cliente_results'] = cliente_results

            # Realiza la búsqueda en Empleado
            empleado_results = Empleado.objects.filter(nombre__icontains=query)
            all_results['empleado_results'] = empleado_results

            # Realiza la búsqueda en Presupuesto
            presupuesto_results = Presupuesto.objects.filter(num__icontains=query)
            all_results['presupuesto_results'] = presupuesto_results

             # Realiza la búsqueda en Presupuesto
            articulo_results = Articulo.objects.filter(tipo_art__icontains=query)
            all_results['articulo_results'] = articulo_results

        return render(request, self.template_name, {'results': all_results, 'query': query})
        

from decimal import Decimal

def calcular_precio_total(articulos):
    horas_totales = sum(articulo.horas * 8 for articulo in articulos)
    precio_madera_total = sum(float(articulo.madera_usada.precio) * articulo.cantidad for articulo in articulos)
    precio_sin_iva = Decimal(horas_totales) + Decimal(precio_madera_total)
    precio_con_iva = precio_sin_iva * Decimal('1.21')

    # Redondear a dos decimales
    precio_con_iva_redondeado = precio_con_iva.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)

    return precio_con_iva_redondeado


def generar_pdf_presupuesto(request, pk):
    # Recupera el presupuesto específico por ID
    presupuesto = get_object_or_404(Presupuesto, pk=pk)

    # Crea el objeto de respuesta PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=Presupuesto_{pk}_informacion.pdf'

    # Crea el objeto PDF usando reportlab
    pdf = canvas.Canvas(response)

    # Agrega contenido al PDF utilizando la información del presupuesto
    y_position = 800

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawCentredString(300, y_position, "MIGUEL ANGEL PERALTA CARPINTERIA")
    y_position -= 40


    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawCentredString(300, y_position, "PRESUPUESTO")
    y_position -= 40

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawCentredString(300, y_position, "INFORMACION DEL CLIENTE")
    y_position -= 40

    pdf.drawString(100, y_position, f"DNI Cliente: {presupuesto.dni_cliente.dni}")
    y_position -= 20

    pdf.drawString(100, y_position, f"Nombre y Apellidos Cliente: {presupuesto.dni_cliente.nombre} {presupuesto.dni_cliente.apellidos}")
    y_position -= 20

    pdf.drawString(100, y_position, f"Telefono Cliente: {presupuesto.dni_cliente.telefono}")
    y_position -= 20

    pdf.drawString(100, y_position, f"Correo Cliente: {presupuesto.dni_cliente.correo}")
    y_position -= 20

    pdf.drawString(100, y_position, f"Direccion Cliente: {presupuesto.dni_cliente.direccion}")
    y_position -= 40

    

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawCentredString(300, y_position, "INFORMACION DEL PEDIDO")
    y_position -= 40

    pdf.drawString(100, y_position, f"Numero de Presupuesto: {presupuesto.num}")
    y_position -= 20

    pdf.drawString(100, y_position, f"Fecha Creacion: {presupuesto.fecha_creacion}")
    y_position -= 20

   # Mostrar información de cada artículo asociado al presupuesto
    pdf.drawString(100, y_position, "Artículos:")
    y_position -= 20

    for articulo in presupuesto.articulos.all():
        pdf.drawString(120, y_position, f"{articulo.tipo_art} DE {articulo.madera_usada.tipos} {articulo.madera_usada.modelo} REALIZDA EN {articulo.horas} HORAS")
        y_position -= 20

    # Precio final
    precio_final = calcular_precio_total(presupuesto.articulos.all())
    pdf.drawString(100, y_position, f"IVA..................................................................................................21%")
    y_position -= 40

    precio_final = calcular_precio_total(presupuesto.articulos.all())
    pdf.drawString(100, y_position, f"Precio Final.................................................................................. {precio_final}")
    y_position -= 300

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawCentredString(300, y_position, "CONFORME LA EMPRESA                 CONFORME EL CLIENTE")
    y_position -= 40

    pdf.showPage()
    pdf.save()

    return response


def generar_pdf_factura(request, pk):
   
    presupuesto = get_object_or_404(Presupuesto, pk=pk)

    # Crea el objeto de respuesta PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=Factura{pk}_informacion.pdf'

    # Crea el objeto PDF usando reportlab
    pdf = canvas.Canvas(response)

    # Agrega contenido al PDF utilizando la información del presupuesto
    y_position = 800

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawCentredString(300, y_position, "MIGUEL ANGEL PERALTA CARPINTERIA")
    y_position -= 40


    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawCentredString(300, y_position, "FACTURA")
    y_position -= 40

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawCentredString(300, y_position, "INFORMACION DEL CLIENTE")
    y_position -= 40

    pdf.drawString(100, y_position, f"DNI Cliente: {presupuesto.dni_cliente.dni}")
    y_position -= 20

    pdf.drawString(100, y_position, f"Nombre y Apellidos Cliente: {presupuesto.dni_cliente.nombre} {presupuesto.dni_cliente.apellidos}")
    y_position -= 20

    pdf.drawString(100, y_position, f"Telefono Cliente: {presupuesto.dni_cliente.telefono}")
    y_position -= 20

    pdf.drawString(100, y_position, f"Correo Cliente: {presupuesto.dni_cliente.correo}")
    y_position -= 20

    pdf.drawString(100, y_position, f"Direccion Cliente: {presupuesto.dni_cliente.direccion}")
    y_position -= 40

    

    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawCentredString(300, y_position, "INFORMACION DEL PEDIDO")
    y_position -= 40

    pdf.drawString(100, y_position, f"Numero de Presupuesto: {presupuesto.num}")
    y_position -= 20

    pdf.drawString(100, y_position, f"Fecha Creacion: {presupuesto.fecha_creacion}")
    y_position -= 20

   # Mostrar información de cada artículo asociado al presupuesto
    pdf.drawString(100, y_position, "Artículos:")
    y_position -= 20

    for articulo in presupuesto.articulos.all():
        pdf.drawString(120, y_position, f"{articulo.tipo_art} DE {articulo.madera_usada.tipos} {articulo.madera_usada.modelo} REALIZDA EN {articulo.horas} HORAS")
        y_position -= 20

    # Precio final
    precio_final = calcular_precio_total(presupuesto.articulos.all())
    pdf.drawString(100, y_position, f"Precio Final: {precio_final}")
    y_position -= 300

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawCentredString(300, y_position, "CONFORME LA EMPRESA                 CONFORME EL CLIENTE")
    y_position -= 40
    # Resto del código...

     # Agrega más contenido según tus necesidades...

    # Cierra el PDF
    pdf.showPage()
    pdf.save()

    return response

#Cookies
from django.http import HttpResponse

def my_view(request):
    response = HttpResponse("Cookie set")
    response.set_cookie('my_cookie', 'cookie_value')
    return response

def another_view(request):
    cookie_value = request.COOKIES.get('my_cookie')
    # Hacer algo con el valor de la cookie
    return HttpResponse("Value of my_cookie: {}".format(cookie_value))

from django.shortcuts import render

def my_view(request):
    return render(request, 'cookies.html', {'show_cookie_notification': True})

from django.shortcuts import render

def my_view(request):
    if 'cookies_accepted' not in request.COOKIES:
        # El usuario aún no ha aceptado las cookies
        # Puedes agregar lógica adicional aquí, si es necesario
        return render(request, 'cookies.html', {'show_cookie_notification': True})
    else:
        # El usuario ya ha aceptado las cookies
        # Puedes hacer algo diferente aquí, como redirigir a otra página
        return render(request, 'cookies.html', {'show_cookie_notification': False})
