# Generated by Django 3.2.19 on 2023-05-31 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_recipeingredientimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredientimage',
            name='image',
            field=models.ImageField(upload_to='recipe/'),
        ),
    ]
