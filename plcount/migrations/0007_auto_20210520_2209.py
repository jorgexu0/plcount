# Generated by Django 2.2.10 on 2021-05-20 21:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plcount', '0006_auto_20210520_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fluxo',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
