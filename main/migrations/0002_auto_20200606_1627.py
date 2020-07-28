# Generated by Django 3.0.7 on 2020-06-06 10:57

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeinfo',
            name='Birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinfo',
            name='Gender',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinfo',
            name='employee_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinfo',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinfo',
            name='user_image',
            field=models.ImageField(upload_to=main.models.get_upload_path),
        ),
    ]