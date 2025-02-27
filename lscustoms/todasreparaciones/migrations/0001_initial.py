# Generated by Django 5.1.5 on 2025-01-28 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Miembro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=60)),
                ('lastname', models.CharField(max_length=60)),
                ('phone', models.IntegerField(null=True)),
                ('joined_date', models.DateField(null=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=16)),
                ('type_user', models.CharField(max_length=50)),
            ],
        ),
    ]
