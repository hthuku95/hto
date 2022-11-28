# Generated by Django 4.0.3 on 2022-11-28 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_author_twitter_handle'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='section',
            name='list_items',
            field=models.ManyToManyField(blank=True, to='articles.listitem'),
        ),
    ]
