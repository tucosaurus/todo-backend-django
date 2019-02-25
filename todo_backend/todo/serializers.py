from rest_framework import serializers


class TodosSerializer(serializers.ModelSerializer):

    class Meta:
        model = None
        fields = (
            'id',
            'todo',
            'description',
            'is_completed',
            'created_at',
            'modified_at'
        )
