# Generated by Django 3.0 on 2021-04-05 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_auto_20210405_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='dosagem',
            field=models.FloatField(verbose_name='Dosagem do Remédio'),
        ),
        migrations.AlterField(
            model_name='receita',
            name='intervalo',
            field=models.FloatField(verbose_name='Intervalo de tempo em horas'),
        ),
    ]
