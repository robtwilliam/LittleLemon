from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK
from restaurant.views import Menu
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User

class MenuViewTest(APITestCase):
    def setup(self):
        Menu.objects.create(title="Coffee",price=4.50)
        Menu.objects.create(title="Muffin",price=3.50)
        
    def test_getall(self):
        url = 'http://127.0.0.1:8000/restaurant/menu/'
        response = self.client.get(url)
        menu = Menu.objects.all()
        serializer = MenuSerializer(menu,many=True)
        self.assertEqual(response.status_code, HTTP_200_OK)
        print(response.data)
        self.assertEqual(response.data,serializer.data)