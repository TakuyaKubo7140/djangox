# Generated by Django 4.2.5 on 2023-12-02 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_alter_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('1', 'カフェ'), ('2', 'レストラン'), ('3', '公園')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='post',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]
