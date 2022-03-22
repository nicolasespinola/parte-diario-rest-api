# Generated by Django 3.2.12 on 2022-03-14 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partediario', '0017_contratistas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entradas',
            old_name='entradas',
            new_name='tipo',
        ),
        migrations.RemoveField(
            model_name='entrada',
            name='entradas',
        ),
        migrations.AddField(
            model_name='entrada',
            name='entradas',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, related_name='entradas', to='partediario.entradas', verbose_name='Entradas'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entrada',
            name='parteDiario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entrada', to='partediario.partediario', verbose_name='Entrada'),
        ),
    ]
