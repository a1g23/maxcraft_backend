# Generated by Django 5.0.3 on 2024-03-30 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=600)),
                ('size', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
