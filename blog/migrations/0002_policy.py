# Generated by Django 2.0.7 on 2018-08-05 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('school', models.CharField(max_length=300)),
                ('department', models.CharField(blank=True, max_length=300)),
                ('administrator', models.CharField(blank=True, max_length=300)),
                ('author', models.CharField(blank=True, max_length=300)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('link', models.URLField()),
                ('published_date', models.DateField(blank=True)),
                ('tags', models.CharField(choices=[('diversity', 'Diversity'), ('admissions', 'Admissions'), ('enrollment', 'Enrollment'), ('faculty', 'Faculty'), ('student affairs', 'Student Affairs'), ('administrative', 'Administrative'), ('fees', 'Fees'), ('data measures', 'Data Measures'), ('international students', 'International Students'), ('academic standards', 'Academic Standards'), ('athletics', 'Athletics'), ('title ix', 'Title IX'), ('accreditation', 'Accreditation')], max_length=50)),
                ('abstract', models.TextField(blank=True)),
                ('text', models.TextField()),
            ],
        ),
    ]
