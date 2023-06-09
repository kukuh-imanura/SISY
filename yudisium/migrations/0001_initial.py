# Generated by Django 4.2.1 on 2023-05-26 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tabelYudisium',
            fields=[
                ('id_yudisium', models.AutoField(primary_key=True, serialize=False)),
                ('transkrip', models.FileField(upload_to='yudisium/transkrip')),
                ('sertifikat_toefl', models.FileField(upload_to='yudisium/toefl/')),
                ('sertifikat_publicSpeaking', models.FileField(upload_to='yudisium/public_speaking/')),
                ('sertifikat_keahlian', models.FileField(upload_to='yudisium/sertifikat_keahlian/')),
                ('sk_bebasPembayaran', models.FileField(upload_to='yudisium/bebas_pembayaran/')),
                ('sk_bebasPinjaman', models.FileField(upload_to='yudisium/bebas_pinjaman/')),
                ('sk_bebasPlagiasi', models.FileField(upload_to='yudisium/bebas_plagiasi/')),
                ('bukti_pembayaran', models.FileField(upload_to='yudisium/pembayaran/')),
            ],
        ),
    ]
