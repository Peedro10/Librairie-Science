# Generated by Django 4.2.1 on 2023-05-17 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0023_rename_account_no_order_n_compte'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caisse',
            old_name='caisse_jour',
            new_name='checkout_day',
        ),
    ]
