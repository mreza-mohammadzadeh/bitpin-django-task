from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.conf import settings
from datetime import timedelta
from django.utils import timezone


class UserManager(BaseUserManager):

    def create_user(self, username, firstname, lastname, password=None):

        if not username:
            raise ValueError('username must have an username')

        user = self.model(username=username, firstname=firstname, lastname=lastname,)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, firstname, lastname, password=None):

        if password is None:
            raise ValueError('password must have an password ')
        user = self.create_user(username, firstname, lastname, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=11, unique=True, null=False, blank=False,)
    firstname = models.CharField(max_length=48, null=False,)
    lastname = models.CharField(max_length=48, null=False,)
    is_active = models.BooleanField(default=True,)
    is_staff = models.BooleanField(default=False,)

    created_time = models.DateTimeField(auto_now_add=True,)
    modified_time = models.DateTimeField(auto_now=True,)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    @classmethod
    def check_user_exist(cls, user):
        try:
            return cls.objects.get(username=user)
        except User.DoesNotExist:
            return None

    @staticmethod
    def create_user(request):
        return User.objects.create(username=request.data['username'], firstname=request.data['firstname'],
                                   lastname=request.data['lastname'])
