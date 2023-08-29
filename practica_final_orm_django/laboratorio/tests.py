from django.test import TestCase, Client
from .models import Laboratorio
from django.urls import reverse

class LaboratorioModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crea datos iniciales para Laboratorio
        Laboratorio.objects.create(nombre="Laboratorio de Prueba", ciudad="Ciudad", pais="Pais")

    def test_nombre_del_laboratorio(self):
        laboratorio = Laboratorio.objects.get(pk=1)
        self.assertEqual(laboratorio.nombre, "Laboratorio de Prueba")


class LaboratorioURLTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        laboratorio = Laboratorio.objects.create(nombre="Laboratorio de Prueba", ciudad="Ciudad", pais="Pais")
        cls.laboratorio_id = laboratorio.id

    def test_confirmar_eliminar_laboratorio_url(self):
        url = reverse('confirmar_eliminar_laboratorio', args=[self.laboratorio_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'confirmar_eliminar_laboratorio.html')

class LaboratorioViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio de Prueba",
            ciudad="Ciudad de Prueba",  # Asegúrate de que coincida con los datos reales
            pais="Pais de Prueba"  # Asegúrate de que coincida con los datos reales
        )
        self.url = reverse('confirmar_eliminar_laboratorio', args=[self.laboratorio.id])


    def test_confirmar_eliminar_laboratorio_view(self):
        response = self.client.get(self.url)
        
        # Verificar que la vista responda con el código de estado 200 (éxito)
        self.assertEqual(response.status_code, 200)

        # Verificar que se esté utilizando la plantilla correcta
        self.assertTemplateUsed(response, 'confirmar_eliminar_laboratorio.html')

        # Imprimir el contenido de la respuesta para depurar
        # print(response.content.decode())

        # Verificar que los datos del laboratorio se muestren en la respuesta HTML
        self.assertContains(response, self.laboratorio.nombre)
