
from django.core.management.base import BaseCommand
from workplace_web.models import PracovniPozice, Firma 

import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('workplace_web/data/data_pracovni_pozice.json', encoding='utf-8') as soubor:
            data_pracovni_pozice = json.load(soubor)
            for pracovni_pozice in data_pracovni_pozice:
                firma_nazev = pracovni_pozice.get("firma")
                
                firma, created = Firma.objects.get_or_create(nazev=firma_nazev)
                
                PracovniPozice.objects.update_or_create(
                    nazev=pracovni_pozice.get("nazev"),
                    mzda=pracovni_pozice.get("mzda"),
                    popis=pracovni_pozice.get("popis"),
                    firma=firma, 
                    misto_prace=pracovni_pozice.get("misto_prace")
                )

    print("Pracovni pozice jsou přidané")
