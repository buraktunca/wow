# Generated by Django 3.0.7 on 2020-09-03 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='altcategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('altcategoryname', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
            ],
            options={
                'db_table': 'altcategory',
            },
        ),
    ]
