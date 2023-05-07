from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):

        products = {'name' : 'apple',
                    'category': 'fruit',
                    'price_for_buy': 500
                    }
        category = {'name': 'fruit',
                    'description': 'its category'}

        Product.objects.all().delete()
        Category.objects.all().delete()

        Product.objects.create(**products)
        Category.objects.create(**category)