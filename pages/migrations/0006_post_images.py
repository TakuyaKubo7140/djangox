# Generated by Django 4.2.5 on 2023-12-03 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_category_alter_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]