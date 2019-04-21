# Generated by Django 2.2 on 2019-04-21 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Approach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('score', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Dicotomic_Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dicotomic_choice', models.PositiveIntegerField(choices=[(5, 'Yes'), (1, 'No')], default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Scale_Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scale_choice', models.PositiveIntegerField(choices=[(5, 'Totally Agree'), (4, 'Agree'), (3, 'Neither agree nor disagree'), (2, 'Disagree'), (1, 'Totally disagree')], default=5)),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('score', models.FloatField()),
                ('approach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kmsurvey.Approach')),
            ],
        ),
        migrations.CreateModel(
            name='Scale_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kmsurvey.Scale_Choice')),
            ],
        ),
        migrations.CreateModel(
            name='Dicotomic_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kmsurvey.Dicotomic_Choice')),
            ],
        ),
    ]