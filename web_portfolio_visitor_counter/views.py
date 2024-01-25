import logging
from .use_cases import CountUseCase
from rest_framework.views import APIView
from rest_framework.response import Response


logger = logging.getLogger(__name__)


class CounterView(APIView):
    def post(self, request):
        ip = request.data.get('ip', None)
        logger.info(f'entroglio, esto es ip {ip}')
        if not ip:
            return Response({'message': 'IP address not provided'}, status=400)
        use_case = CountUseCase()
        try:
            res = use_case.exe(ip)
            return Response(res, status=200)
        except:
            return Response(status=400)
