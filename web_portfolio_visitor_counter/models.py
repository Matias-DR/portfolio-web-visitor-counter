from django.db import models


class CounterModel(models.Model):
    ip = models.GenericIPAddressField(unique=True)
    counter = models.IntegerField(default=1)

    def count(self):
        self.counter += 1
        self.save()
