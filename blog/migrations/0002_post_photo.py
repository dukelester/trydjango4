# Generated by Django 3.1.4 on 2020-12-17 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default=2, upload_to=''),
            preserve_default=False,
        ),
    ]
