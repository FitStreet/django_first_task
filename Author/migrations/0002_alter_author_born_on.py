# Generated by Django 5.0 on 2023-12-12 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Author', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='born_on',
            field=models.DateField(),
        ),
    ]