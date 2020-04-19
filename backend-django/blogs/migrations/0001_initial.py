# Generated by Django 3.0.5 on 2020-04-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('BodyMeta', models.CharField(blank=True, max_length=500, null=True)),
                ('Body', models.TextField()),
                ('DateCreated', models.DateField(auto_now=True)),
            ],
        ),
    ]
