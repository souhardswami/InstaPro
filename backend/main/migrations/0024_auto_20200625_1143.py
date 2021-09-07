# Generated by Django 3.0.6 on 2020-06-25 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagHash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagword', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='tags',
            name='tagword',
        ),
        migrations.AddField(
            model_name='tags',
            name='tagpar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.TagHash'),
        ),
    ]
