# Generated by Django 2.0 on 2018-03-07 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField(db_column='post_title')),
                ('content', models.TextField(db_column='post_content')),
            ],
            options={
                'db_table': 'wp_posts',
            },
        ),
    ]
