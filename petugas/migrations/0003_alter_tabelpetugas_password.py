# Generated by Django 4.2.1 on 2023-05-31 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petugas', '0002_alter_tabelpetugas_tipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabelpetugas',
            name='password',
            field=models.CharField(max_length=32),
        ),
    ]