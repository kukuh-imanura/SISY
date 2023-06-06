# Generated by Django 4.2.1 on 2023-06-06 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sidang', '0006_alter_tabelsidang_nim'),
    ]

    operations = [
        migrations.CreateModel(
            name='tabelWaktuSidang',
            fields=[
                ('id_waktu_sidang', models.AutoField(primary_key=True, serialize=False)),
                ('waktu_sidang', models.TimeField()),
                ('id_sidang', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sidang.tabelsidang')),
            ],
        ),
    ]