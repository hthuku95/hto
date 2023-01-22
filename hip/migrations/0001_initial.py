# Generated by Django 4.0.3 on 2023-01-22 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImprovementProposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('A', 'Approved'), ('D', 'Denied'), ('IQ', 'In Que')], default='IQ', max_length=2)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('priority', models.CharField(blank=True, choices=[('HS', 'Highly Sensitive'), ('S', 'Sensitive'), ('M', 'Medium Priority'), ('L', 'Low Priority'), ('LT', 'Long Term')], max_length=2, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.userprofile')),
            ],
        ),
    ]
