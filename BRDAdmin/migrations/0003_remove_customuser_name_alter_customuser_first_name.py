# Generated by Django 4.0.3 on 2022-04-08 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BRDAdmin', '0002_alter_customuser_employee_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='name',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
    ]