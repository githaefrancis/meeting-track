# Generated by Django 4.0.4 on 2022-05-31 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_rename_task_name_subtask_task_ref_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_block',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='task_in_block', to='tasks.taskblock'),
            preserve_default=False,
        ),
    ]
