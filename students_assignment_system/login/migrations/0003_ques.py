# Generated by Django 3.0.2 on 2020-02-09 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20200209_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='ques',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.IntegerField(default=6)),
                ('ques', models.CharField(max_length=1000)),
                ('i', models.CharField(max_length=100)),
                ('o', models.CharField(max_length=100)),
            ],
        ),
    ]