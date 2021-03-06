# Generated by Django 2.2.6 on 2020-03-13 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Club', '0005_auto_20200313_1623'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['updated_on']},
        ),
        migrations.AlterField(
            model_name='post',
            name='club_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Club.Club'),
        ),
    ]
