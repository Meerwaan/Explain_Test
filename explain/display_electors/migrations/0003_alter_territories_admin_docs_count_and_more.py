# Generated by Django 4.1.3 on 2022-11-24 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display_electors', '0002_territoriesparents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='territories',
            name='admin_docs_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='territories',
            name='articles_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='territories',
            name='code',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='territories',
            name='impacters_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='territories',
            name='population',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='territories',
            name='sources_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='territories',
            name='websites_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='territoriesparents',
            name='child_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='territoriesparents',
            name='parent_id',
            field=models.IntegerField(),
        ),
    ]
