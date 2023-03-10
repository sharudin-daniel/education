# Generated by Django 4.1.5 on 2023-01-31 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_alter_course_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='rightAnswer',
        ),
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('CHOOSE_ANSWERS', 'Choose Answers'), ('WRITE_ANSWERS', 'Write Answers')], default='CHOOSE_ANSWERS', max_length=60),
        ),
        migrations.CreateModel(
            name='TaskResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.task')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.question')),
            ],
        ),
    ]
