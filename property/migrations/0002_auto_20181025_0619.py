# Generated by Django 2.0.1 on 2018-10-25 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='houseownerdetails',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='houseownerdetails',
            name='lastname',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
