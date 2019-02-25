from rest_framework import viewsets, mixins

from . import serializers


class TodosViewSet(
            mixins.RetrieveModelMixin,
            mixins.ListModelMixin,
            mixins.UpdateModelMixin,
            mixins.CreateModelMixin,
            viewsets.GenericViewSet
        ):
    serializer_class = serializers.TodosSerializer
    queryset = None
