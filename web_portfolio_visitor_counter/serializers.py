from rest_framework.serializers import ModelSerializer
from .models import CounterModel


class CounterModelSerializer(ModelSerializer):
    '''
        Serializer for the CounterModel
    '''
    class Meta:
        model = CounterModel
        fields = [
            'ip',
            'counter'
        ]

