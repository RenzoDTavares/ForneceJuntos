# Generated by Django 4.2.13 on 2024-06-04 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ForneceJuntos', '0006_delete_contato'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_contato', models.IntegerField(choices=[(1, 'Telefone'), (2, 'Celular'), (3, 'Email')])),
                ('valor_contato', models.CharField(max_length=255)),
                ('ativo', models.BooleanField(default=True)),
                ('cnpj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ForneceJuntos.fornecedor')),
            ],
        ),
    ]
