from django.db import models


class CounterModel(models.Model):
    """
        Entity/Model for the web portfolio visitor's counter

        Attributes:
            ip (str): IP of visitor.
            counter (int): Number of visits by IP.
    """

    ip = models.GenericIPAddressField(unique=True)
    counter = models.IntegerField(default=0)

    def count(
        self,
        save: bool
    ) -> None:
        """
            Increases the counter by one

            Args:
                save (boolean): Determines if the counter is saved in the database

            Returns:
                None
        """
        self.counter += 1
        if save:
            CounterModel.objects.filter(
                ip=self.ip
            ).update(
                counter=self.counter
            )
