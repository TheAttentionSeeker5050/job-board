# Generated by Django 4.0.4 on 2022-05-05 03:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0008_rename_user_cvupload_user_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0003_alter_company_company_address_and_more'),
        ('jobpost', '0003_jobpost_employer_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobCandidateApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_file_address', models.CharField(max_length=500)),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidate.candidate')),
                ('candidate_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('employer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
    ]