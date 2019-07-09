from django.contrib import admin

from .forms import DocumentForm
from .models import Library, Document

class LibraryAdmin(admin.ModelAdmin):
    pass

class DocumentAdmin(admin.ModelAdmin):
    form = DocumentForm
    list_display = ['title', 'library', 'documents']

admin.site.register(Library, LibraryAdmin)
admin.site.register(Document, DocumentAdmin)
