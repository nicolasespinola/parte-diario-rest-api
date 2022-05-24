# Generated by Django 3.2.13 on 2022-05-20 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partediario', '0004_auto_20220519_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Palpacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_prenadas', models.IntegerField(blank=True, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoriaPalp', to='partediario.categoria', verbose_name='Categoria Palpacion')),
            ],
            options={
                'verbose_name_plural': 'Palpacion',
            },
        ),
    ]