# Generated by Django 5.0.3 on 2024-03-14 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clpmodel',
            old_name='botao',
            new_name='Botao',
        ),
        migrations.RenameField(
            model_name='clpmodel',
            old_name='ligarobo',
            new_name='LigaRobo',
        ),
        migrations.RenameField(
            model_name='clpmodel',
            old_name='reset',
            new_name='ResetContador',
        ),
        migrations.RenameField(
            model_name='clpmodel',
            old_name='sensor',
            new_name='Sensor',
        ),
        migrations.RenameField(
            model_name='clpmodel',
            old_name='value',
            new_name='ValorContagem',
        ),
        migrations.RemoveField(
            model_name='clpmodel',
            name='date',
        ),
    ]