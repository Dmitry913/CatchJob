# Generated by Django 2.2 on 2020-10-13 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.DateField()),
                ('first_name', models.CharField(max_length=32)),
                ('second_name', models.CharField(max_length=32)),
                ('education', models.TextField(max_length=64)),
                ('work_experience', models.TextField(max_length=1024)),
                ('country', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('e_mail', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.DateField()),
                ('name', models.CharField(max_length=32)),
                ('number_vacancy', models.IntegerField()),
                ('country', models.CharField(max_length=32)),
                ('city', models.TextField(max_length=32)),
                ('phone', models.IntegerField()),
                ('e_mail', models.EmailField(max_length=254)),
                ('sphere', models.CharField(max_length=32)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
