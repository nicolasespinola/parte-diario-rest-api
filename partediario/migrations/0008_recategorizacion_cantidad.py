# Generated by Django 3.2.12 on 2022-03-01 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partediario', '0007_recategorizacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='recategorizacion',
            name='cantidad',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]