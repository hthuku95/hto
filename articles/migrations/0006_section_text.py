# Generated by Django 4.0.3 on 2022-09-20 10:39

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_section_code_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='text',
            field=djrichtextfield.models.RichTextField(blank=True, null=True),
        ),
    ]
