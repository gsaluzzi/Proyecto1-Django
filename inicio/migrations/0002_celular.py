# Generated by Django 4.2.6 on 2023-10-29 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Celular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('anio', models.IntegerField()),
            ],
        ),
    ]
