# Generated by Django 4.0.5 on 2022-06-12 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_rename_fingerprint_characteristics_usuario_salvar_digital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='salvar_digital',
            field=models.CharField(blank=True, help_text='Deixe em branco se não quiser salvar a digital', max_length=512),
        ),
    ]
