from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class AuthBackEnd(ModelBackend):
    def authenticate(self, login_id=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email = login_id) or UserModel.objects.get(username=login_id)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
