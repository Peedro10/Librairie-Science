# Generated by Django 3.2.12 on 2023-04-24 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_alter_caisse_caisse_jour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('was_executed_before', models.BooleanField(default=False)),
            ],
        ),
    ]
