# Generated by Django 4.1.1 on 2022-10-13 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created']},
        ),
    ]
