# Generated by Django 4.1.7 on 2023-04-03 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_personas', '0002_alumno_photo_docente_photo_tutor_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='photo',
            field=models.ImageField(default='defaul.jpg', upload_to='alumno'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='photo',
            field=models.ImageField(default='defaul.jpg', upload_to='docentes'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='photo',
            field=models.ImageField(default='defaul.jpg', upload_to='tutor'),
        ),
    ]
