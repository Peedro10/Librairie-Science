# Generated by Django 4.2 on 2023-04-24 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_caisse_caisse_jour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caisse',
            name='caisse_jour',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
