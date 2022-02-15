from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.admin = True
        user.is_superuser = True
        user.is_staff = True
        user.active = True
        user.save(using=self._db)
        return user
