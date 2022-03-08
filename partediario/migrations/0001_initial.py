# Generated by Django 3.2.12 on 2022-03-01 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('representante', models.CharField(max_length=50)),
                ('empresa', models.CharField(max_length=50)),
                ('ruc_empresa', models.CharField(default='0', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Superficie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_totales', models.CharField(max_length=50)),
                ('has_utiles', models.CharField(max_length=50)),
                ('actividad', models.CharField(max_length=50)),
                ('empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='superficies', to='partediario.empresa', verbose_name='Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='parteDiario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha Creada')),
                ('empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='partediario', to='partediario.empresa', verbose_name='Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='lluvia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mm_central', models.PositiveSmallIntegerField(verbose_name="Cant. de mm's de lluvia en la Central:")),
                ('mm_retiro', models.PositiveSmallIntegerField(verbose_name="Cant. de mm's de lluvia en el Retiro:")),
                ('evento', models.CharField(max_length=50, verbose_name='Otro evento:')),
                ('parteDiario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lluvia', to='partediario.partediario', verbose_name='Lluvias')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.CharField(max_length=50)),
                ('pesocab', models.CharField(max_length=50)),
                ('categoria', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='partediario.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parteDiario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entrada', to='partediario.partediario', verbose_name='Entradas')),
            ],
        ),
        migrations.AddField(
            model_name='empresa',
            name='Inventario_de_Empresa',
            field=models.ManyToManyField(to='partediario.Inventario'),
        ),
    ]
