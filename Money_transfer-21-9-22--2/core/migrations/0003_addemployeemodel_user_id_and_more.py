# Generated by Django 4.1 on 2022-10-15 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_addemployeemodel_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='addemployeemodel',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='addemployeemodel',
            name='Address',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='addemployeemodel',
            name='City',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='addemployeemodel',
            name='Country',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='addemployeemodel',
            name='Email',
            field=models.EmailField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='addemployeemodel',
            name='employee_pic',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='addemployeemodel',
            name='password',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='addemployeemodel',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='addemployeemodel',
            name='user_name',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
