# Generated by Django 4.1 on 2022-10-15 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_addemployeemodel_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addemployeemodel',
            name='phone',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='addemployeemodel',
            name='user_id',
            field=models.TextField(null=True),
        ),
    ]
