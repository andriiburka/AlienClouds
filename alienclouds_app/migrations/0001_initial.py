# Generated by Django 3.1.4 on 2020-12-19 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(default='logo.png', upload_to='images')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ShopItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(default='logo.png', upload_to='images')),
                ('description', models.TextField(blank=True)),
                ('price', models.FloatField(blank=True)),
            ],
        ),
    ]
