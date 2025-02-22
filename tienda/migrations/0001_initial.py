# Generated by Django 2.2 on 2024-10-02 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tienda.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCatProd', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Categoría de Producto',
                'verbose_name_plural': 'Categorías de Productos',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomProduct', models.CharField(help_text='Nombre del producto', max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, help_text='Precio del producto', max_digits=10)),
                ('imagen', models.ImageField(blank=True, help_text='Imagen del producto frontal', null=True, upload_to=tienda.models.upload_to)),
                ('ventas_totales', models.IntegerField(default=0)),
                ('descuento', models.IntegerField(default=0, help_text='Descuento')),
                ('stock', models.IntegerField(default=0, help_text='Cantidad disponible en stock')),
                ('sku', models.CharField(help_text='Número único del producto', max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('categorias', models.ManyToManyField(to='tienda.CategoriaProd')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='ReporteVentas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('total_venta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reporte de Ventas',
                'verbose_name_plural': 'Reportes de Ventas',
            },
        ),
    ]
