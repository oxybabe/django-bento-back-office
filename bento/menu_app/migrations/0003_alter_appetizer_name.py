# Generated by Django 4.2.2 on 2023-06-22 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0002_dessert_appetizer_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appetizer',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]