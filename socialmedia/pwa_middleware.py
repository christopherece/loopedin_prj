from django.http import HttpResponse
from django.views.static import serve
from django.conf import settings
import os

class PWAMiddleware:
    """
    Middleware to handle PWA service worker registration and manifest.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_request(self, request):
        if request.path == '/sw.js':
            try:
                return serve(request, 'sw.js', document_root=settings.STATIC_ROOT + '/js')
            except:
                return HttpResponse(status=404)
        return None
