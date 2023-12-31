# Generated by Django 4.2.7 on 2023-11-03 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_adi', models.CharField(max_length=100)),
                ('film_aciklama', models.TextField()),
                ('film_img', models.CharField(max_length=100)),
                ('anasayfa', models.BooleanField(default=False)),
            ],
        ),
    ]
