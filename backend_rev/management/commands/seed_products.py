import random

from django.core.management.base import BaseCommand

from backend_rev.models import Product

ADJECTIVES = [
    "Classic", "Premium", "Compact", "Wireless", "Portable",
    "Smart", "Basic", "Deluxe", "Mini", "Pro",
]

ITEMS = [
    "Mouse", "Keyboard", "Monitor", "Headset", "Webcam",
    "Speaker", "Charger", "Router", "Laptop", "Tablet",
]


class Command(BaseCommand):
    help = "Seed the database with sample products."

    def add_arguments(self, parser):
        parser.add_argument("--count", type=int, default=100)

    def handle(self, *args, **options):
        count = options["count"]
        random.seed(0)

        products = []
        for i in range(count):
            # name is capped at 20 chars, so keep the suffix short.
            name = f"{ADJECTIVES[i % 10]} {ITEMS[(i // 10) % 10]}"
            products.append(
                Product(
                    name=name[:20],
                    price=random.randint(100, 5000),
                    is_available=random.random() < 0.8,
                )
            )

        Product.objects.bulk_create(products)
        self.stdout.write(
            self.style.SUCCESS(f"Created {len(products)} products.")
        )
