# Generated by Django 3.1.1 on 2021-02-16 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_posthome'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posthome',
            old_name='banner_Aboutcarousel_image',
            new_name='banner_Abtimage',
        ),
        migrations.AddField(
            model_name='posthome',
            name='banner_serv',
            field=models.ImageField(default='', upload_to='images/'),
            preserve_default=False,
        ),
    ]