"""
Custom middleware for the social media application.
"""
import re
from django.conf import settings
from django.http import HttpResponse
from django.views.static import serve

class AdminStaticFilesMiddleware:
    """
    Middleware to serve admin static files in production.
    This is a workaround for serving admin static files when DEBUG is False.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # Compile regex for admin static files
        self.admin_static_regex = re.compile(r'^/static/admin/(.*)$')
        
    def __call__(self, request):
        # Check if the request is for admin static files
        match = self.admin_static_regex.match(request.path)
        if match:
            # Extract the path to the static file
            path = match.group(1)
            # Serve the static file directly
            return serve(request, path, document_root=settings.STATIC_ROOT + '/admin/')
        
        # Continue with normal request processing
        return self.get_response(request)
