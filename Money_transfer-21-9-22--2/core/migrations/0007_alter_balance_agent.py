# Generated by Django 4.1 on 2022-10-15 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_expenses_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.addagent'),
        ),
    ]
