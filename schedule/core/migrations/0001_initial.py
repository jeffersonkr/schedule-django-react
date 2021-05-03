# Generated by Django 3.2 on 2021-05-03 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('expertise', models.CharField(choices=[('GNL', 'Clínico Geral'), ('PDN', 'Pediatra'), ('CDT', 'Cardiologista')], default='GNL', max_length=3)),
                ('schedule_work_time', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule_date', models.DateField()),
                ('schedule_time', models.TimeField()),
                ('title', models.CharField(max_length=100)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.doctor')),
            ],
        ),
    ]