# Generated by Django 2.1.2 on 2020-04-04 16:17

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20180930_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='policy',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True),
        ),
        migrations.AlterField(
            model_name='policy',
            name='abstract',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='policy',
            name='administrator',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='policy',
            name='author',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='policy',
            name='department',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='policy',
            name='tags',
            field=models.CharField(choices=[('diversity', 'Diversity'), ('admissions', 'Admissions'), ('enrollment', 'Enrollment'), ('faculty', 'Faculty'), ('student affairs', 'Student Affairs'), ('administrative', 'Administrative'), ('fees', 'Fees'), ('data measures', 'Data Measures'), ('international students', 'International Students'), ('academic standards', 'Academic Standards'), ('athletics', 'Athletics'), ('title ix', 'Title IX'), ('accreditation', 'Accreditation')], max_length=255, null=True),
        ),
        migrations.AddIndex(
            model_name='policy',
            index=django.contrib.postgres.indexes.GinIndex(fields=['search_vector'], name='website_pol_search__746098_gin'),
        ),
    ]
