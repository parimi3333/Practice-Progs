# Generated by Django 4.1.1 on 2022-09-16 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0002_delete_employe_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='employe',
            fields=[
                ('empid', models.IntegerField(primary_key=True, serialize=False)),
                ('empname', models.CharField(max_length=60)),
                ('empsal', models.IntegerField()),
                ('empbranch', models.CharField(max_length=45)),
                ('emprole', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_verified', models.BooleanField(default=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
