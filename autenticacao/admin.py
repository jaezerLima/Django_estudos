from django.contrib import admin
from .models import Pessoa, Cargos, Pedido
# Register your models here.


class PedidoInline(admin.TabularInline):
    readonly_fields = ('nome', 'quantidade', 'descricao')
    list_display = ('nome', 'quantidade', 'descricao')
    model = Pedido
    extra = 0


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    inlines = [PedidoInline]
    list_display = ('get_foto', 'nome', 'email', 'senha', 'nome_completo')
    # readonly_fields = ('senha', 'cargo')
    search_fields = ('nome', 'senha')
    list_filter = ('cargo',)
    list_editable = ('email',)


admin.site.register(Cargos)
