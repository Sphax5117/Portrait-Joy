# Generated by Django 3.1.6 on 2022-07-28 13:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220728_1254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creations',
            old_name='title',
            new_name='titre',
        ),
        migrations.AddField(
            model_name='creations',
            name='cree_a',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
