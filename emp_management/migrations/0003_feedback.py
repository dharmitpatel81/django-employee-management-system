# Generated by Django 4.1.5 on 2023-03-16 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_management', '0002_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('feedback', models.TextField()),
            ],
        ),
    ]
