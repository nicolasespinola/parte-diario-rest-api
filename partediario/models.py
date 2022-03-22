from tabnanny import verbose
from django.db import models


class parteDiario(models.Model):
    fecha = models.DateField("Fecha Creada")

    empresa = models.ForeignKey(
        "partediario.Empresa",
        models.SET_NULL,
        "partediario",
        null=True,
        verbose_name=("Empresa"),
    )

    def __str__(self):
        return 'de {}'.format(self.empresa.empresa)


class Categoria(models.Model):
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.categoria)


class Entradas(models.Model):
    tipo = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Entradas"

    def __str__(self):
        return '{}'.format(self.tipo)


class Salidas(models.Model):
    salidas = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Salidas"

    def __str__(self):
        return '{}'.format(self.salidas)


class opcionSanitacion(models.Model):
    opcion = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Opciones de Sanitacion"

    def __str__(self):
        return '{}'.format(self.opcion)


class lluvia(models.Model):
    mm_central = models.PositiveSmallIntegerField(
        "Cant. de mm's de lluvia en la Central:")
    mm_retiro = models.PositiveSmallIntegerField(
        "Cant. de mm's de lluvia en el Retiro:")
    evento = models.CharField("Otro evento:", max_length=50)

    parteDiario = models.ForeignKey(
        parteDiario, models.CASCADE, "lluvia", verbose_name=("Lluvias")
    )


def __str__(self):
    return '{} {} {}'.format('Lluvia de', self.mm_central, 'mms')


class entrada(models.Model):
    cantidad = models.IntegerField(null=True, blank=True)
    cantidad_M = models.IntegerField(null=True, blank=True)
    cantidad_H = models.IntegerField(null=True, blank=True)
    categoria = models.ManyToManyField(to=Categoria)
    pesoTotal = models.IntegerField(null=True, blank=True)
    parteDiario = models.ForeignKey(
        parteDiario, models.CASCADE, "entrada", verbose_name=("Entrada")
    )
    entradas = models.ForeignKey(
        Entradas, models.CASCADE, "entradas", verbose_name=("Entradas")
    )


class rotacion(models.Model):
    potrero_inicial = models.CharField(max_length=50)
    potrero_final = models.CharField(max_length=50)
    parteDiario = models.ForeignKey(
        parteDiario, models.CASCADE, "rotacion", verbose_name=("Rotacion")
    )

    class Meta:
        verbose_name_plural = "Rotaciones"


class recorrida(models.Model):
    potrero = models.CharField(max_length=50)
    observacion = models.CharField(max_length=120)
    parteDiario = models.ForeignKey(
        parteDiario, models.CASCADE, "recorrida", verbose_name=("Recorrida")
    )


def __str__(self):
    return '{} {}'.format('Entrada de', self.categoria.categoria)


class salida(models.Model):
    salidas = models.ManyToManyField(to=Salidas)
    cantidad = models.IntegerField(null=True, blank=True)
    categoria_madre = models.ManyToManyField(to=Categoria)
    causa = models.CharField(max_length=50)
    parteDiario = models.ForeignKey(
        parteDiario, models.CASCADE, "salida", verbose_name=("Salidas")
    )


class pesaje(models.Model):
    categoria = models.ManyToManyField(to=Categoria)
    cantidad = models.IntegerField(null=True, blank=True)
    peso_minimo = models.IntegerField(null=True, blank=True)
    peso_maximo = models.IntegerField(null=True, blank=True)
    parteDiario = models.ForeignKey(
        parteDiario, models.CASCADE, "pesaje", verbose_name=("Pesajes")
    )


class opcionActividad(models.Model):

    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Actividades"
        verbose_name = "Actividad"

    def __str__(self):
        return '{}'.format(self.nombre)


class otraActividad(models.Model):
    actividad_realizada = models.ManyToManyField(to=opcionActividad)
    categoria = models.ManyToManyField(to=Categoria)
    cantidad = models.IntegerField(null=True, blank=True)
    parteDiario = models.ForeignKey(
        parteDiario, models.CASCADE, "Otra", verbose_name=("Otros")
    )


class sanitacion(models.Model):
    elemento = models.ManyToManyField(to=opcionSanitacion)
    potrero = models.IntegerField(blank=True, null=True)
    observacion = models.CharField(max_length=100, blank=True)
    parteDiario = models.ForeignKey(
        parteDiario, models.CASCADE, "sanitacion", verbose_name=("Sanitacion/Vacunacion")
    )

    def __str__(self):
        return '{}'.format(self.elemento)

    class Meta:
        verbose_name_plural = "Sanitaciones"


class recategorizacion(models.Model):
    categoria_inicial = models.ForeignKey(
        Categoria, models.CASCADE, "inicial", verbose_name=("Recategorizacion Inicial")
    )
    categoria_final = models.ForeignKey(
        Categoria, models.CASCADE, "final", verbose_name=("Recategorizacion Final")
    )
    cantidad = models.IntegerField(null=True, blank=True)
    parteDiario = models.ForeignKey(
        parteDiario, models.CASCADE, "recategorizacion", verbose_name=("Recategorizacion")
    )

    class Meta:
        verbose_name_plural = "Recategorizaciones"

    def __str__(self):
        return '{}'.format(self.categoria_inicial)


class Inventario(models.Model):
    categoria = models.ManyToManyField(to=Categoria)
    cantidad = models.CharField(max_length=50)
    pesocab = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.cantidad)


class Potrero(models.Model):
    franja = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '{} {}'.format("Potero N. ", self.franja)


class Empresa(models.Model):
    representante = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    ruc_empresa = models.CharField(max_length=50, default='0')
    Inventario_de_Empresa = models.ManyToManyField(
        to=Inventario, null=True, blank=True)
    potreros = models.IntegerField(blank=True)

    def __str__(self):
        return '{}'.format(self.empresa)


class Superficie(models.Model):
    has_totales = models.CharField(max_length=50)
    has_utiles = models.CharField(max_length=50)
    actividad = models.CharField(max_length=50)
    empresa = models.ForeignKey(
        "partediario.Empresa",
        models.SET_NULL,
        "superficies",
        null=True,
        verbose_name=("Empresa"),
    )

    def __str__(self):
        return '{} {} {}'.format('Superficie ', self.has_totales, ' has')


class contratistas(models.Model):
    trabajos_realizados = models.CharField(max_length=50)
    insumos = models.CharField(max_length=50)
    parteDiario = models.ForeignKey(
        parteDiario, models.CASCADE, "contratista", verbose_name=("Contratistas")
    )