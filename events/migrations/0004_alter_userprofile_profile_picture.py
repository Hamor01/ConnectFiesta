# Generated by Django 4.2.7 on 2023-11-15 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_eventcategory_eventtag_remove_event_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
