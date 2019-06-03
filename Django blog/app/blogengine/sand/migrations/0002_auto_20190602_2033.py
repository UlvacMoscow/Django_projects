# Generated by Django 2.0.7 on 2019-06-02 17:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupElements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='groupghost',
            name='element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sand.GroupElements'),
            preserve_default=False,
        ),
    ]
