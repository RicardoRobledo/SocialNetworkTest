# Generated by Django 3.2 on 2022-05-15 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grupo', '0007_alter_mivista_grupo'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrupoRespaldo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_grupo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('propietario', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='mivista',
            options={'managed': False},
        ),
    ]
