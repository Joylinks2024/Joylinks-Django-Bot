# Generated by Django 5.0.4 on 2024-04-20 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0004_alter_user_total_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='olimpiada',
            field=models.BooleanField(default=False),
        ),
    ]
