# Generated by Django 3.2.12 on 2022-03-08 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partediario', '0012_alter_empresa_potreros'),
    ]

    operations = [
        migrations.CreateModel(
            name='opcionSanitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcion', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Opciones de Sanitacion',
            },
        ),
        migrations.CreateModel(
            name='sanitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('potrero', models.IntegerField(blank=True, null=True)),
                ('causa', models.CharField(max_length=50)),
                ('categoria_madre', models.ManyToManyField(to='partediario.Categoria')),
                ('elemento', models.ManyToManyField(to='partediario.opcionSanitacion')),
                ('parteDiario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sanitacion', to='partediario.partediario', verbose_name='Sanitacion/Vacunacion')),
            ],
        ),
    ]