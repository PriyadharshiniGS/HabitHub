# Generated by Django 4.1 on 2024-04-16 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0026_alter_habit_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='status',
            field=models.CharField(default='In progress', max_length=255),
        ),
    ]
