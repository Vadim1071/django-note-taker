# Generated by Django 5.1.1 on 2025-02-24 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_folder_notes_folder_user_note_folder'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-created_at'], 'verbose_name': 'заметка', 'verbose_name_plural': 'заметки'},
        ),
    ]
