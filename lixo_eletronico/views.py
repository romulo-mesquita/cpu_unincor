from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from datetime import datetime
from .forms import ContatoForm 
from .models import(
	Eventos,
	EventosRealizados,
	Imagens,
	Parcerias,
	)


def index(request):
    return render(request, 'lixo_eletronico/home.html')

def base(request):
	parceria = Parcerias.objects.all()
	context = {'parceria': parceria,}
	print (context)

	return render(request, 'lixo_eletronico/base.html', context)

def eventos(request):
	data_atual = datetime.now()
	print(data_atual)
	agendas = Eventos.objects.filter(data_evento__gte=data_atual)
	realizados = Eventos.objects.filter(data_evento__lt=data_atual)

	context = {
		'agendas': agendas,
		'realizados': realizados,
	}

	return render(request, 'lixo_eletronico/eventos.html', context)

def agenda_completa(request):
	data_atual = datetime.now()
	eventos = Eventos.objects.filter(data_evento__gte=data_atual)

	context = {'eventos':eventos}

	return render(request, 'lixo_eletronico/agenda_completa.html', context)

def evento_detalhe(request, eventos_id):
	evento = get_object_or_404(Eventos, pk=eventos_id)

	context = {'evento':evento}

	return render(request, 'lixo_eletronico/evento_detalhe.html', context)

def contato(request):
	if request.method == 'GET':
		form = ContatoForm()
	else:
		form = ContatoForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['assunto']
			from_email = form.cleaned_data['email']
			message = form.cleaned_data['menssagem']
			try:
				send_mail(subject, message, from_email, ['romulo.mesquita@unincor.edu.br'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('lixo_eletronico/success')
	return render(request, "lixo_eletronico/contato.html", {'form': form})

def success(request):
    return HttpResponse('Success! Thank you for your message.')

def grupo(request):
	return render(request, 'lixo_eletronico/grupo_estudo.html')
