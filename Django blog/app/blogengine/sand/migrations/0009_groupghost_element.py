# Generated by Django 2.0.7 on 2019-06-02 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sand', '0008_remove_groupghost_element'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupghost',
            name='element',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sand.GroupElements'),
        ),
    ]
