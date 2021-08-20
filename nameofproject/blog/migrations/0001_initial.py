# Generated by Django 3.0.6 on 2021-08-20 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=300)),
                ('post_date', models.DateTimeField()),
                ('post_text', models.TextField()),
                ('post_image', models.ImageField(upload_to='event_images/')),
            ],
        ),
    ]
