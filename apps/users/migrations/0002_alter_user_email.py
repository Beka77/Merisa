# Generated by Django 4.1 on 2023-03-29 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
