# Generated by Django 5.0 on 2024-01-11 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_by', models.CharField(max_length=30)),
                ('post_content', models.CharField(max_length=20)),
                ('publish_date', models.CharField(max_length=30)),
                ('comments', models.CharField(max_length=20)),
            ],
        ),
    ]