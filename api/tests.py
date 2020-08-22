from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product

# Create your tests here.

# Testing simple GETs first - List products
class ProductListTestCase(APITestCase):
    def test_product_list(self):
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class AvailableProductListTestCase(APITestCase):
    def test_available_products(self):
        response = self.client.get(reverse('product-list-available'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class SoldOutProductListTestCase(APITestCase):
    def test_unavailable_products(self):
        response = self.client.get(reverse('product-list-soldout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Testing registering a product via POST method
class RegisterProductTestCase(APITestCase):
    def test_product_register(self):
        data = {'sku': 'SomeSKU', 'name': 'Some Prod', 'quantity': '3', 'price': '450'}
        response = self.client.post(reverse('product-register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response.data)

# Testing GET method by specific SKUs
class ProductDetailsTestCase(APITestCase):
    def setUp(self):
        Product.objects.create(sku='SomeSKU', name='Some Prod', quantity='3', price='450')
    def test_product_details(self):
        response = self.client.get(reverse('product-details', kwargs={'pk': 'SomeSKU'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Finally, testing for our PATCH method
class ProductQuantityChange(APITestCase):
    def setUp(self):
        Product.objects.create(sku='SomeSKU', name='Some Prod', quantity='3', price='450')

    def test_product_quantity_change(self):
        response = self.client.patch(reverse('product-quantity-change',
            kwargs={'pk': 'SomeSKU', 'quantity': -1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
