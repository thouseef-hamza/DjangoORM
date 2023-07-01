# Generated by Django 4.2.2 on 2023-07-01 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ormapp', '0002_alter_student_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('benevolence_factor', models.PositiveSmallIntegerField(default=50, help_text='How benevolent this hero is?')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ormapp.category')),
            ],
        ),
    ]