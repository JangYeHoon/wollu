# Generated by Django 4.1.4 on 2023-01-03 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_jobstats_job_stats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('min_wollu', models.IntegerField()),
                ('max_wollu', models.IntegerField()),
                ('total_wollu', models.IntegerField()),
                ('user_num', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Job_Stats',
        ),
    ]
