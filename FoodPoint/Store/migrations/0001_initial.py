# Generated by Django 3.2.3 on 2021-05-30 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Store_name', models.TextField()),
                ('Store_tel', models.TextField()),
                ('Store_add', models.TextField()),
                ('Store_num', models.TextField()),
            ],
        ),
    ]
