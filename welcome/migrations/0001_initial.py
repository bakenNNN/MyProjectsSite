# Generated by Django 4.1.2 on 2023-01-09 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WelcomeText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('welcome_header', models.CharField(max_length=150)),
                ('welcome_text', models.CharField(max_length=1500)),
            ],
        ),
    ]