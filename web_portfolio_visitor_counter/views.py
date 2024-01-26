import logging

from .exceptions import Exception
from .use_cases import countUseCase
from rest_framework.views import APIView
from rest_framework.response import Response


logger = logging.getLogger(__name__)


class CounterView(APIView):
    """
        View for the visit count
    """

    def post(self, request):
        """
            Gets ip from body and executes de use case of count
        """
        # Si como "data" envían cualquier cosa que NO sea un objeto JSON,
        # se rompe, por eso las sentencias try-except para "data.get(...)".
        try:
            ip = request.data.get('ip', None)
            if not ip:
                return Response(
                    {'message': 'IP address not provided'},
                    status=400
                )
        except:
            return Response(
                {'message': 'IP address not provided'},
                status=400
            )
        try:
            res = countUseCase(ip)
            logger.info(f'\n {res} \n')
            return Response(res, status=200)
        except Exception as e:
            return Response(
                {'message': e.msg},
                status=e.status_code
            )
