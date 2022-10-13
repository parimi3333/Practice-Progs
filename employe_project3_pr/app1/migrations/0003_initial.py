# Generated by Django 4.1.1 on 2022-09-13 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0002_remove_enrolement_branch_remove_enrolement_employe_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='enrolement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.branch')),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.employe')),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='employes',
            field=models.ManyToManyField(through='app1.enrolement', to='app1.employe'),
        ),
    ]
