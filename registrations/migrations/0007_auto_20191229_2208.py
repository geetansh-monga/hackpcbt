# Generated by Django 3.0.1 on 2019-12-29 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0006_auto_20191229_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='year',
            field=models.CharField(choices=[('first', 'First'), ('second', 'Second'), ('third', 'Third'), ('fourth', 'Four')], max_length=10),
        ),
    ]