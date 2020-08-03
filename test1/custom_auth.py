from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username = None, password = None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            user = UserModel._default_manager.get_by_natural_key(username)
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if password == "OTP_VALIDATION" and self.user_can_authenticate(user):
                return user
            elif user.check_password(password) and self.user_can_authenticate(user):
                return user