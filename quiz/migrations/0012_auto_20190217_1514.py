# Generated by Django 2.1.2 on 2019-02-17 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_auto_20190217_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='quiz_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.quizid'),
        ),
    ]
