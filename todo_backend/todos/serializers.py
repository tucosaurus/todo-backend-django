# Third Party Stuff
from rest_framework import serializers

from . import models


class TodosSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Todo
        fields = (
            'id',
            'todo',
            'description',
            'is_completed',
            'created_at',
            'modified_at'
        )
