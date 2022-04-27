from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User


class parteDiario(models.Model):
    fecha = models.DateField("Fecha Creada")

    empresa = models.ForeignKey(
        "partediario.Empresa",
        models.SET_NULL,
        "partediario",
        null=True,
        verbose_name=("Empresa"),
    )

    lluvia = models.ForeignKey(
        "partediario.lluvia",
        models.SET_NULL,
        "partediario",
        null=True,
        blank=True,
        verbose_name=("Lluvias"),
    )

    entrada = models.ForeignKey(
        "partediario.entrada",
        models.SET_NULL,
        "partediario",
        null=True,
        blank=True,
        verbose_name=("Entrada"),
    )

    salida = models.ForeignKey(
        "partediario.salida",
        models.SET_NULL,
        "partediario",
        null=True,
        blank=True,
        verbose_name=("Salida"),
    )

    recategorizacion = models.ForeignKey(
        "partediario.recategorizacion",
        models.SET_NULL,
        "partediario",
        null=True,
        blank=True,
        verbose_name=("Recategorizacion"),
    )

    rotacion = models.ForeignKey(
        "partediario.rotacion",
        models.SET_NULL,
        "partediario",
        null=True,
        blank=True,
        verbose_name=("Rotacion"),
    )

    sanitacion = models.ForeignKey(
        "partediario.sanitacion",
        models.SET_NULL,
        "partediario",
        null=True,
        blank=True,
        verbose_name=("Sanitacion"),
    )

    contratistas = models.ForeignKey(
        "partediario.contratistas",
        models.SET_NULL,
        "partediario",
        null=True,
        blank=True,
        verbose_name=("Contratistas"),
    )

    recorrida = models.ForeignKey(
        "partediario.recorrida",
        models.SET_NULL,
        "partediario",
        null=True,
        blank=True,
        verbose_name=("Recorridas"),
    )

    opcionSanitacion = models.ForeignKey(
        "partediario.opcionSanitacion",
        models.SET_NULL,
        "partediario",
        null=True,
        blank=True,
        verbose_name=("Opcion de Sanitacion"),
    )

    def __str__(self):
        return 'de {}'.format(self.empresa.empresa)


class Capataz(models.Model):
    user = models.OneToOneField(
        User, related_name="usuario", on_delete=models.CASCADE, verbose_name="Usuario")
    phone = models.IntegerField(null=True, blank=True)
    empresaCapataz = models.ForeignKey(
        "partediario.Empresa",
        related_name="Empresa",
        on_delete=models.CASCADE,
        blank=True,
        verbose_name=("Empresa asociada")
    )

    def __str__(self):
        return self.user.first_name


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


def __str__(self):
    return '{} {} {}'.format('Lluvia de', self.mm_central, 'mms')


class entrada(models.Model):
    cantidad = models.IntegerField(null=True, blank=True)
    cantidad_m = models.IntegerField(null=True, blank=True)
    cantidad_h = models.IntegerField(null=True, blank=True)
    peso_total = models.IntegerField(null=True, blank=True)
    categoria = models.ForeignKey(
        Categoria, models.CASCADE, related_name="categorias_entrada", verbose_name=("Categorias")
    )
    entradas = models.ForeignKey(
        Entradas, models.CASCADE, "entradas", verbose_name=("Entradas")
    )


class rotacion(models.Model):
    potrero_inicial = models.CharField(max_length=50)
    potrero_final = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Rotaciones"


class recorrida(models.Model):
    potrero = models.CharField(max_length=50)
    observacion = models.CharField(max_length=120)


def __str__(self):
    return '{} {}'.format('Entrada de', self.categoria.categoria)


class salida(models.Model):
    cantidad = models.IntegerField(null=True, blank=True)
    causa = models.CharField(max_length=50)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name="categorias_salida", verbose_name=("Categorias")
    )
    salidas = models.ForeignKey(
        Salidas, models.CASCADE, "tipo_salidas", verbose_name=("Salidas")
    )


class pesaje(models.Model):
    categoria = models.ForeignKey(
        Categoria, models.CASCADE, "categorias_pesaje", verbose_name=("Categorias")
    )
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
    categoria = models.ForeignKey(
        Categoria, models.CASCADE, "categorias_Otro", verbose_name=("Categorias")
    )
    actividad = models.ForeignKey(
        opcionActividad, models.CASCADE, "opciones", verbose_name=("Opciones")
    )
    cantidad = models.IntegerField(null=True, blank=True)
    parteDiario = models.ForeignKey(
        parteDiario, models.CASCADE, "Otra", verbose_name=("Otros")
    )


class sanitacion(models.Model):
    elemento = models.ForeignKey(
        opcionSanitacion, models.CASCADE, "elemento_de_sanitacion", verbose_name=("Elementos de Sanitacion")
    )
    potrero = models.IntegerField(blank=True, null=True)
    observacion = models.CharField(max_length=100, blank=True)

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

    class Meta:
        verbose_name_plural = "Recategorizaciones"

    def __str__(self):
        return '{}'.format(self.categoria_inicial)


class Inventario(models.Model):
    categoria = models.ForeignKey(
        Categoria, models.CASCADE, "categorias_inventario", verbose_name=("Categorias")
    )
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
        to=Inventario, blank=True)
    potreros = models.IntegerField(blank=True, null=True)

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
