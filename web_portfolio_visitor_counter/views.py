import logging

from .models import CounterModel
from .serializers import CounterModelSerializer
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


logger = logging.getLogger(__name__)


class CounterView(
    CreateModelMixin,
    ListModelMixin,
    GenericViewSet
):
    queryset = CounterModel.objects.all()
    serializer_class = CounterModelSerializer

    def perform_create(
            self,
            serializer: CounterModelSerializer
    ) -> None:
        '''
            Creates a new CounterModel instance if the IP is not in the database
            or increments the counter if the IP is already in the database.
        '''

        ip = serializer.validated_data['ip']
        logger.info(f'Visita realizada por {ip}.')
        counter = self.queryset.filter(ip=ip).first()
        if counter is not None:
            counter.count(True)
            serializer.instance = counter
        else:
            serializer.save()

    def list(
        self,
        request: Request,
        *args,
        **kwargs
    ) -> Response:
        '''
            Lists the counter
        '''

        logger.info(f'Se listó el contador.')
        return super().list(request, *args, **kwargs)
