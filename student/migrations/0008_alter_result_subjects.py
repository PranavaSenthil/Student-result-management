# Generated by Django 3.2.20 on 2023-08-31 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_alter_result_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='subjects',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='student.subject'),
        ),
    ]
