# Generated by Django 3.1.6 on 2022-08-27 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_delete_accueil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creations',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
