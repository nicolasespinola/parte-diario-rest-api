from django.core.management.base import BaseCommand, CommandError
from partediario.models import parteDiario
import csv


class Command(BaseCommand):
    def handle(self, *args, **options):
