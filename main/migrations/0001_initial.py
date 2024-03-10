# Generated by Django 5.0.2 on 2024-03-09 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numerator', models.FloatField(verbose_name='Чисельник')),
                ('denominator', models.FloatField(verbose_name='Знаменник')),
            ],
        ),
    ]