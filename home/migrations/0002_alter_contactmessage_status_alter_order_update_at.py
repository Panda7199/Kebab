# Generated by Django 4.0 on 2022-01-07 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='status',
            field=models.CharField(choices=[('New', 'Yangi'), ('Read', 'O`qilgan'), ('Closed', 'Yopilgan')], default='New', max_length=15),
        ),
        migrations.AlterField(
            model_name='order',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
