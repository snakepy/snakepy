# Generated by Django 2.2.3 on 2019-07-25 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YourModelNameHere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_1st_field_name_here', models.TextField(blank=True, default='', null=True)),
                ('your_2nd_field_name_here', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]
