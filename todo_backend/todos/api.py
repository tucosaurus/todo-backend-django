# Third Party Stuff
from rest_framework import mixins, viewsets

from . import models, serializers


class TodosViewSet(
            mixins.RetrieveModelMixin,
            mixins.ListModelMixin,
            mixins.UpdateModelMixin,
            mixins.CreateModelMixin,
            mixins.DestroyModelMixin,
            viewsets.GenericViewSet
        ):
    serializer_class = serializers.TodosSerializer
    queryset = models.Todo.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
