# Generated by Django 3.1.1 on 2021-02-17 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210216_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postabout',
            name='banner_Abtimage',
        ),
        migrations.RemoveField(
            model_name='postabout',
            name='banner_carAboutImage',
        ),
        migrations.RemoveField(
            model_name='posthome',
            name='banner_homeImage',
        ),
        migrations.RemoveField(
            model_name='posthome',
            name='banner_review_image',
        ),
        migrations.RemoveField(
            model_name='postservice',
            name='banner_serv',
        ),
        migrations.RemoveField(
            model_name='postvision',
            name='banner_Visimage',
        ),
        migrations.AddField(
            model_name='postabout',
            name='banner_Abtimage1',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='postabout',
            name='banner_Abtimage2',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='postabout',
            name='banner_Abtimage3',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='postabout',
            name='banner_carAboutImage1',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='postabout',
            name='banner_carAboutImage2',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='postabout',
            name='banner_carAboutImage3',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='postabout',
            name='banner_carAboutImage4',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='postabout',
            name='banner_carAboutImage5',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='posthome',
            name='banner_homeImage1',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='posthome',
            name='banner_homeImage2',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='posthome',
            name='banner_homeImage3',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='posthome',
            name='banner_review_image1',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='posthome',
            name='banner_review_image2',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='posthome',
            name='banner_review_image3',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='postservice',
            name='banner_serv1',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='postservice',
            name='banner_serv2',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='postservice',
            name='banner_serv3',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='postvision',
            name='banner_Visimage1',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='postvision',
            name='banner_Visimage2',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='postvision',
            name='banner_Visimage3',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
    ]