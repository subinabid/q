# Generated by Django 2.1.2 on 2019-01-13 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20190114_0016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answers',
            old_name='date',
            new_name='ans_date',
        ),
    ]
