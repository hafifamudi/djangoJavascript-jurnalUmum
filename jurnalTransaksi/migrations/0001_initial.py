# Generated by Django 3.0.3 on 2020-02-15 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jurnalApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='transaksiJurnal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggalJurnal', models.DateField()),
                ('uraianJurnal', models.TextField()),
                ('debt', models.FloatField(blank=True, default=0.0)),
                ('kredit', models.FloatField(blank=True, default=0.0)),
                ('jurnal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaksis', to='jurnalApp.Jurnal')),
            ],
            options={
                'db_table': 'transaksi',
                'ordering': ['-id'],
            },
        ),
    ]
