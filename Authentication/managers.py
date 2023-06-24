from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, *args, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, *args, **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, *args, **kwargs):
        return self.create_user(email, password, is_staff=True, is_superuser=True, *args, **kwargs)