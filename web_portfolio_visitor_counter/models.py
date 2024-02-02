import logging

from django.db import models


logger = logging.getLogger(__name__)


class CounterModel(models.Model):
    '''
        Entity/Model for the web portfolio visitor's counter

        Attributes:
            ip (str): IP of visitor.
            counter (int): Number of visits by IP.
    '''

    ip = models.GenericIPAddressField()
    counter = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.ip} - {self.counter}'

    def count(
        self,
        save: bool
    ) -> None:
        '''
            Increases the counter by one

            Args:
                save (boolean): Determines if the counter is saved in the database

            Returns:
                None
        '''
        logger.info(f'Contador de {self.ip} incrementado.')
        self.counter += 1
        if save:
            CounterModel.objects.filter(
                ip=self.ip
            ).update(
                counter=self.counter
            )
