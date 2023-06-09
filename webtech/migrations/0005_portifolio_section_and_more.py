# Generated by Django 4.2 on 2023-05-14 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtech', '0004_contact_delete_contactmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portifolio_section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('project_image', models.ImageField(upload_to='static/img')),
            ],
        ),
        migrations.RemoveField(
            model_name='portifolio_detail',
            name='project_name',
        ),
        migrations.AlterField(
            model_name='portifolio_detail',
            name='project_image',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]
