# Generated by Django 4.2.2 on 2023-07-24 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_student_pass_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='pass_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]