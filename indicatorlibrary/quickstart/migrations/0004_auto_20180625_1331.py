# Generated by Django 2.0.2 on 2018-06-25 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0003_auto_20180625_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicator',
            name='name',
            field=models.TextField(max_length=1000),
        ),
    ]
