# Generated by Django 4.0.6 on 2022-08-04 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0013_rename_post_updated_post_updated_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(),
        ),
    ]
