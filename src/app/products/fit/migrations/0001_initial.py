# Generated by Django 3.1.5 on 2021-01-26 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.PositiveSmallIntegerField(choices=[(1, 'Very Small'), (2, 'Small'), (3, 'Good'), (4, 'Big'), (5, 'Very Big')])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductFit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=2, max_digits=3)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', unique=True)),
            ],
        ),
    ]
