# Generated by Django 2.1.2 on 2019-01-13 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_ans',
            field=models.TextField(default='Answer'),
            preserve_default=False,
        ),
    ]
