# Generated by Django 4.0.4 on 2022-04-20 23:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('candidate', '0005_alter_cvupload_candidate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvupload',
            name='candidate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
