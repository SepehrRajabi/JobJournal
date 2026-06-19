from django.contrib.auth.base_user import BaseUserManager
from typing import Optional


class UserManager(BaseUserManager):
    def create_user(
            self,
            first_name: str,
            last_name: str,
            password: Optional[str] = None,
            is_superuser: bool = False,
            is_admin: bool = False,
            is_staff: bool = False,
            is_active: bool = True,
            *args,
            **kwargs
    ):
        if not first_name:
            raise ValueError("first name must be providede")

        if not last_name:
            raise ValueError("last name must be providede")

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            *args,
            **kwargs
        )
        user.set_password(password)
        user.is_superuser = is_superuser
        user.is_admin = is_admin
        user.is_staff = is_staff
        user.is_active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        first_name: str,
        last_name: str,
        password: str,
        is_superuser: bool = True,
        is_admin: bool = True,
        is_staff: bool = True,
        is_active: bool = True,
        *args,
        **kwargs
    ):
        return self.create_user(
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_superuser=is_superuser,
            is_admin=is_admin,
            is_staff=is_staff,
            is_active=is_active,
            *args,
            **kwargs
        )
