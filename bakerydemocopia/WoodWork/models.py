from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Madera(models.Model):
    #MADERAS
    TROPICALES='Tropicales'
    TRATADAS='Tratadas'
    FRONDOSAS='Frondosas' 
    CONIFERAS='Coniferas'
        
    TIPO_MADERA = ( 
        (TROPICALES, 'Tropicales'), 
        (TRATADAS, 'Tratadas' ), 
        (FRONDOSAS, 'Frondosas'), 
        (CONIFERAS, 'Coniferas'),
        )
    ###############################################

    #TROPICALES
    EBANO='Ebano'
    CAOBA='Caoba'
    PALISANDRO='Palisandro' 
    ZEBRANO='Zebrano'

    #TRATADAS
    TRAVIESAS='Traviesas'
    VIGAS_TABLAS='Vigas Tratadas'
    PALOS_CILINDRICOS='Palos Cilindricos' 
    LISTON='Liston'

    #FRONDOSAS
    ROBLE_ROJO_FLAS='Roble Rojo Flas'
    ROBLE_BLANCO_FLAS='Roble Blanco Flas'
    FRONDOSO='Frondoso' 
    CIRCULAR_IROKO='Circular Iroko'
    CIRCULAR_CASTANO='Circulas Castaño'
    OLMO_FLITCHES='Olmo Flitches'
    HAYA_VAPORIZADA='Haya Vaporizada' 
    FRESNO_FAS='Fresno Flas'
    CASTANO_FLITCHES='Castaño FLitches'

    #CONIFERAS    
    ALERCE='Alerce'
    PINO='Pino'
    PINO_AMARILLO='Pino Amarillo' 

    MODELO_MADERA = ( 

    (EBANO,'Ebano'),
    (CAOBA,'Caoba'),
    (PALISANDRO,'Palisandro'),
    (ZEBRANO,'Zebrano'),

    #TRATADAS
    (TRAVIESAS,'Traviesas'),
    (VIGAS_TABLAS, 'Tratadas'),
    (PALOS_CILINDRICOS, 'Palos Cilindricos'), 
    (LISTON, 'Liston'),

    #FRONDOSAS
    (ROBLE_ROJO_FLAS, 'Roble Rojo Flas'),
    (ROBLE_BLANCO_FLAS,'Roble Blanco Flas'),
    (FRONDOSO, 'Frondoso'), 
    (CIRCULAR_IROKO, 'Circular Iroko'),
    (CIRCULAR_CASTANO, 'Circulas Castaño'),
    (OLMO_FLITCHES, 'Olmo Flitches'),
    (HAYA_VAPORIZADA, 'Haya Vaporizada'), 
    (FRESNO_FAS, 'Fresno Flas'),
    (CASTANO_FLITCHES, 'Castaño FLitches'),

    #CONIFERAS    
    (ALERCE, 'Alerce'),
    (PINO, 'Pino'),
    (PINO_AMARILLO,'Pino Amarillo'),

        )

    referencia = models.CharField(max_length= 10)
    tipos = models.CharField(max_length=100, choices=TIPO_MADERA)
    modelo = models.CharField(max_length=200, choices=MODELO_MADERA)
    tamano = models.DecimalField(max_digits=6, decimal_places=2)
    img = models.ImageField('foto', height_field=None, blank=True, null=True)
    precio= models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.referencia} | {self.tipos} | {self.modelo} | {self.tamano}m"

    def get_absolute_url(self):
        return reverse("madera-detail", kwargs={"pk": self.pk})

class Cliente(models.Model):
    dni= models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono= models.CharField(max_length=9)
    correo = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return f"{self.dni} | {self.nombre} | {self.apellidos}"

    def get_absolute_url(self):
        return reverse("cliente-detail", kwargs={"pk": self.pk})

class Empleado(models.Model):
    dni= models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    correo = models.CharField(max_length=200, blank=True, null=True)
    telefono= models.CharField(max_length=9)


    def __str__(self):
        return f"{self.dni} | {self.nombre} | {self.apellidos}"

    def get_absolute_url(self):
        return reverse("empleado-detail", kwargs={"pk": self.pk})

class Articulo(models.Model):
    tipo_art = models.CharField(max_length=100)
    madera_usada = models.ForeignKey(Madera, related_name="usada", on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    horas = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField('foto', height_field=None, blank=True, null=True)


    def __str__(self):
        return f"{self.tipo_art} - {self.madera_usada.modelo} - {self.horas} horas"

    def get_absolute_url(self):
        return reverse("articulo-detail", kwargs={"pk": self.pk})

class Presupuesto(models.Model):
    num = models.IntegerField(default=0)
    dni_cliente = models.ForeignKey(Cliente, related_name="DNI_clientes", on_delete=models.CASCADE)
    articulos = models.ManyToManyField(Articulo)
    fecha_creacion = models.DateField(auto_now_add=True)
    precio_final = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Nuevo campo para el precio final

    def __str__(self):
        return f"{self.dni_cliente} | {self.fecha_entrega} | {self.precio_final}€"

    def get_absolute_url(self):
        return reverse("presupuesto-detail", kwargs={"pk": self.pk})
    


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField()
    nombre_completo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)
