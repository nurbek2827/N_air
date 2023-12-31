# Generated by Django 4.2.3 on 2023-08-24 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_n_air', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sneakers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('image', models.ImageField(upload_to='')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('character', models.TextField()),
                ('price_type', models.CharField(choices=[("so'm", "so'm"), ('$', '$'), ('₽', '₽')], default="so'm", max_length=128)),
                ('price', models.IntegerField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_n_air.category')),
            ],
        ),
    ]
