# Generated by Django 4.2 on 2023-04-24 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_caisse_return_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='caisse',
            name='caisse_jour',
            field=models.IntegerField(default=0),
        ),
    ]
