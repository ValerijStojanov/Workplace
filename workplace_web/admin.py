from django.contrib import admin
from .models import Firma, PracovniPozice, editor_text
from ckeditor.widgets import CKEditorWidget
from django.db import models

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

admin.site.register(Firma)
admin.site.register(PracovniPozice)
admin.site.register(editor_text, MyModelAdmin)
