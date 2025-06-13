from django.contrib.auth.models import User


class EmailAuthBackend:
    def authenticate(self, request, username=None,password=None):
        pass

    def get_user(self):
        pass
