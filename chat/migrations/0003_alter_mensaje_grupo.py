# Generated by Django 3.2 on 2022-04-11 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grupo', '0002_auto_20220410_1344'),
        ('chat', '0002_auto_20220410_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grupo.grupo'),
        ),
    ]
