from django.contrib import admin
from .models import(
	Eventos,
	EventosRealizados,
	Imagens,
	Parcerias,
	)

class EventosAdmin(admin.ModelAdmin):
	model = Eventos

class EventosRealizadosAdmin(admin.ModelAdmin):
	model = EventosRealizados

class ImagensAdmin(admin.ModelAdmin):
	model = Imagens

class ParceriasAdmin(admin.ModelAdmin):
	model = Parcerias

	
admin.site.register(Eventos, EventosAdmin)
admin.site.register(EventosRealizados, EventosRealizadosAdmin)
admin.site.register(Imagens, ImagensAdmin)
admin.site.register(Parcerias, ParceriasAdmin)