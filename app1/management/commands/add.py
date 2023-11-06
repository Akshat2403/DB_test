# add_dummy_data.py
from django.core.management.base import BaseCommand
from app1.models import Product
import random

class Command(BaseCommand):
    help = 'Add dummy data to the Product model'

    def handle(self, *args, **options):
        products = []
        for i in range(1, 31):
            product_data = {
                'name': f'Product {i}',
                'description': f'Description for Product {i}',
                'price': round(random.uniform(10, 100), 2),
            }
            products.append(product_data)

        for product_data in products:
            Product.objects.create(
                name=product_data['name'],
                description=product_data['description'],
                price=product_data['price']
            )

        self.stdout.write(self.style.SUCCESS('Successfully added 30 instances of dummy data to the Product model.'))
