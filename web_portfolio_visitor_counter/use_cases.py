from .exceptions import GenericErrorException
from .models import CounterModel


def countUseCase(ip: str):
    """
        Increases the counter by one if the IP is already registered,
        otherwise creates a new record in the database with the IP and
        counter in 1.

        Args:
            ip (str): IP of visitor.

        Returns:
            {
                'ip': str,
                'counter': int
            }
    """
    try:
        result = CounterModel.objects.get_or_create(ip=ip)
        counter = result[0]
        counter.count(save=True)
    except:
        raise GenericErrorException
    return {
        'ip': ip,
        'counter': counter.counter
    }
