# Generated by Django 4.0.3 on 2022-03-06 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=30)),
                ('produto', models.CharField(max_length=20)),
                ('valor', models.IntegerField(max_length=6)),
            ],
        ),
    ]
