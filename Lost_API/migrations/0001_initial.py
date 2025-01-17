# Generated by Django 5.0.2 on 2025-01-11 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('found', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='True', max_length=5)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('img', models.ImageField(upload_to='uploads/')),
                ('data', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('location', models.CharField(max_length=255)),
                ('comments', models.JSONField(default=list)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
