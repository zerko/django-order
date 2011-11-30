from django.core.management.base import BaseCommand, CommandError
from order.utils import is_orderable, create_order_objects
from django.db.models import get_model

class Command(BaseCommand):
    args = '<app.model>'
    help = 'Create order items for objects already present in the database.'

    def handle(self, *args, **options):
        label = args[0]
        order_fields = is_orderable(label)
        if order_fields:
            create_order_objects(get_model(*label.split('.')), order_fields)