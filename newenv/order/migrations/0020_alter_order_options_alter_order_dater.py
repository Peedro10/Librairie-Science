# Generated by Django 4.2.1 on 2023-05-12 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0019_order_dater'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created', 'dater')},
        ),
        migrations.AlterField(
            model_name='order',
            name='dater',
            field=models.DateField(blank=True, null=True),
        ),
    ]
