# Generated by Django 5.1.6 on 2025-03-10 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_rename_telefone_cliente_celular_alter_cliente_cpf_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=255)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
