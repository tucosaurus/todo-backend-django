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

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
