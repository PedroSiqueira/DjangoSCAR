# Generated by Django 4.0.5 on 2022-06-11 21:50

from django.db import migrations, models
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='permissao',
            options={'verbose_name_plural': 'permissoes'},
        ),
        migrations.AddField(
            model_name='usuario',
            name='fingerprint_characteristics',
            field=models.CharField(default=None, max_length=512, validators=[web.models.validar_impressao_digital]),
            preserve_default=False,
        ),
    ]
