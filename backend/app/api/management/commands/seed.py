from django.core.management.base import BaseCommand # type: ignore
from api.models import Document

initial_data = [
    {"type": "bank-draft", "title": "Bank Draft", "position": 0},
    {"type": "bill-of-lading", "title": "Bill of Lading", "position": 1},
    {"type": "invoice", "title": "Invoice", "position": 2},
    {"type": "bank-draft-2", "title": "Bank Draft 2", "position": 3},
    {"type": "bill-of-lading-2", "title": "Bill of Lading 2", "position": 4},
]

class Command(BaseCommand):
    help = 'Seed initial data'

    def handle(self, *args, **kwargs):
        for item in initial_data:
            Document.objects.get_or_create(
                type=item['type'],
                title=item['title'],
                position=item['position']
            )
        self.stdout.write(self.style.SUCCESS('Data seeded successfully'))
