# Generated by Django 2.2.5 on 2021-08-18 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210818_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=100)),
                ('products', models.ManyToManyField(to='store.Product')),
            ],
            options={
                'ordering': ['cat_name'],
            },
        ),
    ]
