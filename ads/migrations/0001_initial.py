# Generated by Django 5.1.2 on 2025-05-05 16:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=500)),
                ('Сreated_at', models.DateField(default=None)),
                ('User', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ads.category')),
                ('Сondition_st', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ads.condition')),
            ],
        ),
    ]
