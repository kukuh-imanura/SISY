# Generated by Django 4.2.1 on 2023-05-31 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahasiswa', '0002_rename_fakultas_tabelmhs_fakultas_alter_tabelmhs_nim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabelmhs',
            name='password',
            field=models.CharField(max_length=32),
        ),
    ]
