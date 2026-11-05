from django.db import models

# Creacion de modelos

class genero(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del genero")

    def __str__(self):
        return self.nombre
    
    class Meta: 
        verbose_name = "Genero"
        verbose_name_plural = "Generos"

class pelicula(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Titulo de la pelicula")
    genero = models.ForeignKey(genero, on_delete=models.CASCADE, verbose_name="Genero de la pelicula")
    imagen_afiche = models.ImageField(upload_to='afiches/', verbose_name="Imagen del afiche")
    precio_entrada = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio de la entrada")
    en_cartelera = models.BooleanField(default=True, null=True, verbose_name="En cartelera")
    sinopsis = models.TextField(blank=True, null=True, verbose_name="Sinopsis de la pelicula")

    def __str__(self):
        estado = "En cartelera" if self.en_cartelera else "No en cartelera"
        return f"{self.titulo} - {estado}"

    class Meta:
        verbose_name = "Pelicula"
        verbose_name_plural = "Peliculas"

class ticket(models.Model):
    pelicula = models.ForeignKey(pelicula, on_delete=models.CASCADE, verbose_name="Pelicula del ticket")
    nombre_comprador = models.CharField(max_length=100, verbose_name="Nombre del comprador")
    correo_comprador = models.EmailField(verbose_name="Correo del comprador")
    cantidad_entradas = models.PositiveIntegerField(verbose_name="Cantidad de entradas")
    fecha_compra = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de compra")
    codigo = models.CharField(max_length=10, unique=True, verbose_name="Codigo del ticket")

    def __str__(self):
        return f"Ticket {self.codigo} para {self.pelicula.titulo} - Comprador: {self.nombre_comprador}"

    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
