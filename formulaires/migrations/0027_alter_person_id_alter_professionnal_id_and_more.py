# Generated by Django 4.2.4 on 2023-08-29 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulaires', '0026_auto_20230616_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='professionnal',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='scolaire',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='spirit',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]