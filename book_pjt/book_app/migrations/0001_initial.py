# Generated by Django 4.2.2 on 2023-06-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('author', models.CharField(max_length=50, null=True)),
                ('cover', models.ImageField(blank=True, upload_to='image')),
                ('price', models.IntegerField()),
                ('is_published', models.BooleanField(default=False)),
            ],
        ),
    ]
