from django.db import models

# Create your models here.
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)
    ciudad = models.CharField(max_length=30, blank=True, null=True)
    pais = models.CharField(max_length=30, blank=True, null=True)
    
    def __str__(self):
        return self.nombre
        
class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=30, blank=True, null=True)
    especialidad = models.CharField(max_length=30, blank=True, null=True)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
        
class Producto(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=False)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.SET_NULL, blank=True, null=True)
    f_fabricacion = models.PositiveIntegerField()
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(f_fabricacion__gte=2015),
                name="fecha_fabricacion_min_2015"
            )
        ]