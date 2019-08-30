from django.db import models

# Create your models here.

class Eventos(models.Model):
	nome_evento = models.CharField('Nome do Evento', max_length=200, null=False, blank=False)
	data_evento = models.DateTimeField('Data do Evento', null=False, blank=False)
	descricao = models.CharField('Descrição do Evento', max_length=500, null=True, blank=True)
	localizacao = models.CharField('Endereço do Evento', max_length=500, null=False, blank=False)

	def get_eventosrealizados(self):
		q = EventosRealizados.objects.filter(
			evento__id=self.id
			)
		
		return q

	def __str__(self):
		return self.nome_evento

class EventosRealizados(models.Model):
	evento = models.ForeignKey(Eventos, null=True, related_name='realizados', on_delete=models.SET_NULL)
	relato = models.TextField('Oque foi realizado no evento?', blank=False, null=True)
	
	def get_imagens(self):
		q = Imagens.objects.filter(
			evento_realizado__id=self.id
			)
		
		return q

	def __str__(self):
		return self.evento.nome_evento

class Imagens(models.Model):
	evento_realizado = models.ForeignKey(EventosRealizados,related_name='imagens', on_delete=models.CASCADE)
	imagem = models.ImageField('Imagem',upload_to = 'static/images/eventos/', height_field=None, width_field=None, blank=False, null=True)

	def __str__(self):
		return self.evento_realizado


class Parcerias(models.Model):
	nome_parceiro = models.CharField('Parceiro', max_length=200, null=True, blank=False)
	logo = models.ImageField('Logo',upload_to = 'static/images/parcerias/', height_field=None, width_field=None, max_length=100, blank=False, null=True)

	def __str__(self):
		return self.nome_parceiro