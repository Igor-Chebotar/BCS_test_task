# Generated by Django 4.1 on 2022-08-19 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bcs_id', models.IntegerField()),
                ('description', models.TextField(max_length=500, null=True)),
            ],
        ),
    ]
