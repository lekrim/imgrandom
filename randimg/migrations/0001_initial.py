# Generated by Django 3.0 on 2020-04-04 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_type', models.CharField(max_length=25)),
                ('img_size', models.CharField(max_length=25)),
                ('img_category', models.CharField(max_length=25)),
                ('img_name', models.CharField(max_length=50)),
            ],
        ),
    ]
