from django.contrib import admin

from loja.models import Produto, Fornecedor

admin.site.register(Produto)
admin.site.register(Fornecedor)
# Register your models here.
