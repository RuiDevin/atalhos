from django.contrib import admin

from atalhos.models import Bairro, Estado, ZonaEstado, ZonaCidade, Rua, Cidade, Endereco, DDD47, Operadora, Nickname

admin.site.register(Bairro)
admin.site.register(Rua)
admin.site.register(ZonaCidade)
admin.site.register(ZonaEstado)
admin.site.register(Estado)
admin.site.register(Cidade)
admin.site.register(Endereco)
admin.site.register(DDD47)
admin.site.register(Operadora)
admin.site.register(Nickname)