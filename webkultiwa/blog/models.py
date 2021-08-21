from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name = 'Título')
    description = models.TextField(verbose_name = 'Descripción')
    image = models.ImageField(verbose_name = 'Imagen', upload_to="entradas")
    link = models.URLField(verbose_name="Dirección Web", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Creado')
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Actualizado')

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ["-created"]

    def __str__(self):
        return self.title
