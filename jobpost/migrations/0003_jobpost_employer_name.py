# Generated by Django 4.0.4 on 2022-04-21 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_alter_company_company_address_and_more'),
        ('jobpost', '0002_alter_jobpost_employer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='employer_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
    ]