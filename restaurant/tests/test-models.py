from django.tests import TestCase
from restaurant.models import Menu


# Menu Items Test
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=10, inventory=10)
        self.assertEqual(item, "IceCream : 80")
