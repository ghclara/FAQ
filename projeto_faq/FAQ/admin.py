from django.contrib import admin
from FAQ.models import Topico, Resposta, Comentario

class ComentarioInLine(admin.TabularInline):
	model = Comentario
	extra = 0
	

class RespostaInLine(admin.TabularInline):
	model = Resposta
	extra = 0
	
	#inlines = [ComentarioInLine]	

class PerguntaAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields': ['pergunta', 'pergunta_data', 'usuario']}), 
	]
	inlines = [RespostaInLine, ComentarioInLine]
	search_fields = ['pergunta']
	#inlines = [ComentarioInLine]

	
admin.site.register(Topico, PerguntaAdmin)
#admin.site.register(Resposta)

