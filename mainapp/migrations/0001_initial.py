# Generated by Django 3.0.7 on 2020-09-03 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('categoryname', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='creator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('creativename', models.CharField(max_length=200)),
                ('üye_date', models.DateTimeField(auto_now_add=True)),
                ('üye_foto', models.ImageField(upload_to='üyeler/')),
            ],
            options={
                'db_table': 'creator',
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('productname', models.CharField(max_length=200)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('oldprice', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.creator')),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
