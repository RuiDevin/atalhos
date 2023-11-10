from django.contrib import admin

from atalhos.models import Bairro, Estado, ZonaEstado, ZonaCidade, Rua, Cidade, Endereco

admin.site.register(Bairro)
admin.site.register(Rua)
admin.site.register(ZonaCidade)
admin.site.register(ZonaEstado)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Endereco)