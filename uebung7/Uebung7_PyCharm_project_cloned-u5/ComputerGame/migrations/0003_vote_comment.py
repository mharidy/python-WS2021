# Generated by Django 3.1.2 on 2021-01-25 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ComputerGame', '0002_comment_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='comment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ComputerGame.comment'),
            preserve_default=False,
        ),
    ]