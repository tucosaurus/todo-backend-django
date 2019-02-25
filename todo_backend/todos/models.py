from django.db import models

from todo_backend.base.models import TimeStampedUUIDModel
# Create your models here.


class Todo(TimeStampedUUIDModel):
    todo = models.CharField(
        max_length=150,
        help_text='Name of this todo'
    )
    description = models.TextField(
        blank=True,
        help_text='Description of this todo'
    )
    is_completed = models.BooleanField(
        default=False,
        help_text='Designates whether this todo has been completed'
    )

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
        ordering = ('-created_at',)
