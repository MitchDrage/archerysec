# Generated by Django 3.1.2 on 2020-10-03 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networkscanners', '0012_auto_20201002_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='nessus_targets_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scan_id', models.TextField(blank=True)),
                ('rescan_id', models.TextField(blank=True, null=True)),
                ('target', models.TextField(blank=True)),
                ('project_id', models.TextField(blank=True)),
                ('date_time', models.DateTimeField(null=True)),
                ('total_dup', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(max_length=256, null=True)),
                ('project_name', models.TextField(blank=True, null=True)),
                ('total_vuln', models.IntegerField(blank=True, null=True)),
                ('total_high', models.IntegerField(blank=True, null=True)),
                ('total_medium', models.IntegerField(blank=True, null=True)),
                ('total_low', models.IntegerField(blank=True, null=True)),
                ('report_name', models.TextField(blank=True)),
            ],
        ),
    ]
