# Generated by Django 4.0 on 2022-01-06 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_file_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='books.subject'),
        ),
    ]