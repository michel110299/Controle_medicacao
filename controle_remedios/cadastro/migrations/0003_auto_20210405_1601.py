# Generated by Django 3.0 on 2021-04-05 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_auto_20210405_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='intervalo',
            field=models.FloatField(default=0, verbose_name='Intervalo de tempo em horas'),
        ),
    ]
