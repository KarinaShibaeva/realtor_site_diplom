# Generated by Django 3.2 on 2023-06-10 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flats_sale', '0013_auto_20230610_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='object',
            name='category_name',
        ),
        migrations.AddField(
            model_name='category',
            name='object_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='flats_sale.object', verbose_name='Объект'),
            preserve_default=False,
        ),
    ]
