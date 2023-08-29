from laboratorio.models import Laboratorio, DirectorGeneral, Producto

# Obtén todos los objetos de Laboratorio
todos_laboratorios = Laboratorio.objects.all()

# Obtén todos los objetos de DirectorGeneral
todos_directores = DirectorGeneral.objects.all()

# Obtén todos los objetos de Producto
todos_productos = Producto.objects.all()

# Obtén el laboratorio del Producto cuyo nombre es 'Producto 1'
laboratorio_producto_1 = Producto.objects.get(nombre='Producto 1').laboratorio

# Ordena todos los productos por nombre y muestra los valores de nombre y laboratorio
productos_ordenados = Producto.objects.order_by('nombre')
for producto in productos_ordenados:
    print(f'Nombre: {producto.nombre}, Laboratorio: {producto.laboratorio.nombre}')

# Imprime los laboratorios de todos los productos
for producto in todos_productos:
    print(f'Producto: {producto.nombre}, Laboratorio: {producto.laboratorio.nombre}')