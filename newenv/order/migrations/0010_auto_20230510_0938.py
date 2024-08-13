# Generated by Django 3.2.12 on 2023-05-10 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_rule'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Rule',
        ),
    ]
