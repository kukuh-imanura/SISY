# Generated by Django 4.2.1 on 2023-05-31 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mahasiswa', '0003_alter_tabelmhs_password'),
        ('yudisium', '0002_tabelyudisium_nim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabelyudisium',
            name='nim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mahasiswa.tabelmhs', unique=True),
        ),
    ]
