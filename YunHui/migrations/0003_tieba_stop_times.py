# Generated by Django 2.0.7 on 2018-08-06 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YunHui', '0002_auto_20180806_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='tieba',
            name='stop_times',
            field=models.IntegerField(default=0, null=True, verbose_name='暂停次数'),
        ),
    ]
