from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify
# Create your models here.

class SlugNazevModel(models.Model):
    nazev = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nazev

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nazev)

        super().save(*args, **kwargs)

class Firma(SlugNazevModel): 
    popis = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=200, blank=True, null=True)

class PracovniPozice(SlugNazevModel):
    mzda = models.CharField(max_length=200, blank=True, null=True)
    popis = RichTextField()
    firma = models.ForeignKey(Firma, on_delete=models.PROTECT, blank=True, null=True)
    datum_tvorby = models.DateTimeField(auto_now_add=True)
    misto_prace = models.CharField(max_length=100, blank=True, null=True)

class editor_text(models.Model):
    content = RichTextField()


# ABY ODSTRANIT MODELY Z PROJEKTU -> MUSÍME SMAZAT db.sqlite3 a ve složce migrations SMAZAT vše kromě __init__.py !!!!