# Generated by Django 4.1.1 on 2022-09-06 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=20)),
                ('pcost', models.IntegerField()),
                ('pmfdt', models.DateField()),
                ('pexpdt', models.DateField()),
            ],
        ),
    ]
