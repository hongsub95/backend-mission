# Generated by Django 4.0.1 on 2022-01-21 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=13)),
                ('market_url', models.URLField(verbose_name='사이트')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
