# Generated by Django 2.2.4 on 2019-08-26 14:25

from django.db import migrations, models
import django.db.models.deletion
import geoposition.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_evento', models.CharField(max_length=200, verbose_name='Nome do Evento')),
                ('data_evento', models.DateTimeField(verbose_name='Data do Evento')),
                ('descricao', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descrição do Evento')),
                ('localizacao', geoposition.fields.GeopositionField(max_length=42)),
            ],
        ),
        migrations.CreateModel(
            name='EventosRealizados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relato', models.TextField(null=True, verbose_name='Oque foi realizado no evento?')),
                ('evento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lixo_eletronico.Eventos')),
            ],
        ),
        migrations.CreateModel(
            name='Imagens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(null=True, upload_to='', verbose_name='Imagem')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lixo_eletronico.EventosRealizados')),
            ],
        ),
    ]
