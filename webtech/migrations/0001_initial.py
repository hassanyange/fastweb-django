# Generated by Django 4.2 on 2023-05-13 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portifolio_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('client', models.CharField(max_length=255)),
                ('project_Date', models.DateField(auto_now_add=True)),
                ('project_url', models.URLField(blank=True)),
                ('project_Info', models.CharField(max_length=255)),
            ],
        ),
    ]