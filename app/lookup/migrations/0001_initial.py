# Generated by Django 5.0.6 on 2024-06-16 06:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=10)),
                ('masc_form', models.CharField(blank=True, max_length=100)),
                ('masc_meaning', models.CharField(blank=True, max_length=100)),
                ('fem_form', models.CharField(blank=True, max_length=100)),
                ('fem_meaning', models.CharField(blank=True, max_length=100)),
                ('neut_form', models.CharField(blank=True, max_length=100)),
                ('neut_meaning', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Spelling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spelling', models.CharField(max_length=50)),
                ('words', models.ManyToManyField(to='lookup.word')),
            ],
        ),
    ]
