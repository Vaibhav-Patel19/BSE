from django.test import TestCase
from .models import *
from django.contrib.auth.models import User


# views Tests
class URLTests(TestCase):

    def test_HomePage(self):
        response = self.client.get('/home/', follow = True) 
        self.assertEqual(response.status_code, 200)

        # If you set follow to True the client will follow any redirects 
        # and a redirect_chain attribute will be set in the response object 
        # containing tuples of the intermediate urls and status codes.

    def test_ExplorePage(self):
        response = self.client.get('/explore/', follow = True)
        self.assertEqual(response.status_code, 200)

    def test_OrderPage(self):
        response = self.client.get('/order/', follow = True)
        self.assertEqual(response.status_code, 200)

    
# Models Tests
class ModelTests(TestCase):
    def test_bar_order_data(self):
        user = User.objects.create(
            username = 'testuser', 
            email = 'testuser@example.com', 
            password = 'test12345'
        )

        order = barOrder.objects.create(
            user = user,
            drinkName = "Bira",
            drinkType = "Beer",
            price = 299,
            quantity = 1
        )

    def test_food_order_data(self):
        user = User.objects.create(
            username = 'testuser', 
            email = 'testuser@example.com', 
            password = 'test12345'
        )

        order = foodOrder.objects.create(
                user = user,
                dishName = "Gulab Jaamun",
                price = 199,
                quantity = 1,
                cooked = False
        )

    
