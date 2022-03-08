# Generated by Django 3.2.12 on 2022-03-01 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partediario', '0002_auto_20220301_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='cantidad',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entrada',
            name='cantidad_H',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entrada',
            name='cantidad_M',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='entrada',
            name='categoria',
            field=models.ManyToManyField(to='partediario.Categoria'),
        ),
        migrations.AddField(
            model_name='entrada',
            name='pesoTotal',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
