from django.contrib import admin
from rcp.webapp.models import Pessoa

# Register your models here.

class PessoaModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'telefone', 'data_nascimento', 'criado_em')
    list_filter = ('criado_em', 'atualizado_em')
    search_fields = ('nome', 'email', 'cpf', 'telefone')
    ordering = ('nome',)
    readonly_fields = ('criado_em', 'atualizado_em')
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('nome', 'email', 'cpf', 'data_nascimento', 'telefone', 'endereco')
        }),
        ('Timestamps', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',),
        }),
    )

admin.site.register(Pessoa, PessoaModelAdmin)

admin.site.site_header = "Administração Geral"
admin.site.site_title = "Administração do Site"
