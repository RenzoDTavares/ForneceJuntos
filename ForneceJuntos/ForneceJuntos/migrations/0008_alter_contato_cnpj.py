# Generated by Django 4.2.13 on 2024-06-05 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ForneceJuntos', '0007_contato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='cnpj',
            field=models.ForeignKey(db_column='cnpj_id', on_delete=django.db.models.deletion.CASCADE, to='ForneceJuntos.fornecedor'),
        ),
    ]
