import logging

from .models import CounterModel
from .lib.exceptions import NotExistException


logger = logging.getLogger(__name__)


class CountUseCase:
    def exe(self, ip: str):
        try:
            CounterModel.objects.create(ip)
        except Exception as exception:
            logger.info(f'ESTA ES LA EXCEPCION: {type(exception)}')
            raise NotExistException()
