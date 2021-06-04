# Generated by Django 3.2.3 on 2021-06-04 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos/%m/%d')),
                ('user', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]
