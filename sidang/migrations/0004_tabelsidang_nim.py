# Generated by Django 4.2.1 on 2023-05-31 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mahasiswa', '0003_alter_tabelmhs_password'),
        ('sidang', '0003_alter_tabelsidang_bukti_pembayaran_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabelsidang',
            name='nim',
            field=models.ForeignKey(default=211001000, on_delete=django.db.models.deletion.CASCADE, to='mahasiswa.tabelmhs'),
            preserve_default=False,
        ),
    ]
