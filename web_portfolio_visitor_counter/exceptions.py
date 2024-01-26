class Exception(BaseException):
    """
        Base exception for all custom exceptions in this project.

        Attributes:
            status_code (str): HTTP code representing the error.
            msg (int): Coloquial message of error.
            es_msg (str, optional): Mensaje coloquial que describe el error.
    """

    def __init__(
        self,
        status_code: int,
        msg: str,
        es_msg: str = ''
    ):
        """
            Args:
                status_code (str): HTTP code representing the error.
                msg (int): Coloquial message of error.
                es_msg (str, optional): Mensaje coloquial que describe el error.
        """
        super().__init__()
        self.status_code = status_code
        self.msg = msg
        self.es_msg = es_msg


class GenericErrorException(Exception):
    """
        Exception used as a generic error

        Attributes:
            status_code (str): HTTP code representing the error.
            msg (int): Coloquial message of error.
            es_msg (str, optional): Mensaje coloquial que describe el error.
    """

    def __init__(self):
        super().__init__(
            500,
            'An error has ocurred.',
            'Ah ocurrido un error.'
        )
        ...
