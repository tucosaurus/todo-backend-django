# Generated by Django 2.1.7 on 2019-02-25 15:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('todo', models.CharField(help_text='Name of this todo', max_length=150)),
                ('description', models.TextField(blank=True, help_text='Description of this todo')),
                ('is_completed', models.BooleanField(default=False, help_text='Designates whether this todo has been completed')),
            ],
            options={
                'verbose_name': 'Todo',
                'verbose_name_plural': 'Todos',
                'ordering': ('-created_at',),
            },
        ),
    ]
