# Generated by Django 4.1.7 on 2023-04-03 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_cursos', '0006_alter_curso_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
