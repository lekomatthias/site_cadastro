# Generated by Django 5.1.6 on 2025-03-05 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=100)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
    ]
