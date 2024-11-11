import logging
from django.utils.timezone import now

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f'[{now()}] URL: {request.path} | Method: {request.method} | User: {request.user}')
        
        response = self.get_response(request)

        return response
