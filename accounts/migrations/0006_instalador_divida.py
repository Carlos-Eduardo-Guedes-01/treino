# Generated by Django 4.1.6 on 2023-02-22 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_instalador_cidade_delete_cidade_delete_estado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='instalador',
            name='divida',
            field=models.FloatField(null=True),
        ),
    ]
