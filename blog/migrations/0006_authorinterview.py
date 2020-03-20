# Generated by Django 3.0.2 on 2020-02-01 09:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorInterview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AuthorName', models.CharField(max_length=150)),
                ('Interview', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('BookName', models.TextField()),
            ],
        ),
    ]
