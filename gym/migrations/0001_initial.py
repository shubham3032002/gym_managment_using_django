# Generated by Django 5.0.2 on 2024-10-23 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GYM_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('m_number', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('plan', models.CharField(max_length=25)),
                ('gender', models.CharField(max_length=25)),
            ],
        ),
    ]