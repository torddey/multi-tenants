# Generated by Django 5.1.4 on 2024-12-25 19:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        ('clients', '0002_alter_products_description_alter_products_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='tenant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='app.clients'),
            preserve_default=False,
        ),
    ]