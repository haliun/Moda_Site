__author__ = 'haliun'
from django.conf import settings

def media_root(request):
    """
    Adds media-root context variables to the context.

    """
    return {'MEDIA_ROOT': settings.MEDIA_ROOT}
