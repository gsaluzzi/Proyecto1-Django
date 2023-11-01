# Generated by Django 4.2.6 on 2023-10-31 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0006_tablet_delete_tablets'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accesorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='tablet',
            name='descripcion',
            field=models.CharField(max_length=100),
        ),
    ]
