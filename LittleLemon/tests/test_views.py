from django.test import TestCase
from restaurant.views import MenuItemView
from restaurant.models import MenuItem

class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        MenuItem.objects.create(title="Burger", price=120, inventory=50)

    def test_getall(self):
        # Get all the menu objects
        menu_items = MenuItem.objects.all()
        # Serialize the menu items
        serialized = [item.serialize() for item in menu_items]
        # Make a GET request to the MenuView
        response = self.client.get('/menu/')
        # Assert that the serialized menu items are equal to the response data
        self.assertEqual(response.data, serialized)