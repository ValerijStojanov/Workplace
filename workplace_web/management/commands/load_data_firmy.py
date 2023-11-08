
from django.core.management.base import BaseCommand
from workplace_web.models import Firma
import json

class Command(BaseCommand):
    def handle(self, **options):
        with open('workplace_web/data/data_firmy.json', encoding='utf-8') as soubor:
            data_firmy = json.load(soubor)
            for data in data_firmy:
                Firma.objects.update_or_create(
                nazev = data.get("nazev"),
                popis = data.get("popis"),
                email = data.get("email"),
                phone_number = data.get("phone_number")
                )
    print('Ok')


# SPOUŠTĚNÍ SCRIPTU python3 manage.py load_data_firmy