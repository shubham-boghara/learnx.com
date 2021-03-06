# Generated by Django 4.0 on 2022-01-05 15:53

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_alter_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorylist',
            name='name',
            field=models.CharField(max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='categorylist',
            name='slug',
            field=models.SlugField(blank=True, max_length=80),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=froala_editor.fields.FroalaField(),
        ),
        migrations.AlterField(
            model_name='subcategorylist',
            name='name',
            field=models.CharField(max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategorylist',
            name='slug',
            field=models.SlugField(blank=True, max_length=80),
        ),
    ]
