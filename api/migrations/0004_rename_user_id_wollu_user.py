# Generated by Django 4.1.4 on 2022-12-27 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_wollu_coffe_alter_wollu_no_work_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wollu',
            old_name='user_id',
            new_name='user',
        ),
    ]
