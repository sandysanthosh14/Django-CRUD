# Generated by Django 4.2 on 2023-08-02 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='cls',
            new_name='sclass',
        ),
    ]
