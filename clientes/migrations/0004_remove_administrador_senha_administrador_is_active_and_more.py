# Generated by Django 5.1.6 on 2025-03-11 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_administrador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administrador',
            name='senha',
        ),
        migrations.AddField(
            model_name='administrador',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='administrador',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='administrador',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='administrador',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='administrador',
            name='password',
            field=models.CharField(default='', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
