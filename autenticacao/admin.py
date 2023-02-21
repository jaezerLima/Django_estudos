from django.contrib import admin
from .models import Pessoa, Cargos
# Register your models here.


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'senha')
    readonly_fields = ('senha', 'cargo')
    search_fields = ('nome', 'senha')
    list_filter = ('cargo',)
    list_editable = ('email',)

admin.site.register(Cargos)
