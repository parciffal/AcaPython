#
from django.db import models
from django.contrib.auth.models import User

#
import datetime


class UserModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media/users', blank=True, null=True)
    registrated_at = models.DateTimeField(default=datetime.datetime.now())
    verify_code = models.TextField(default='')
    
    def __str__(self) -> str:
        return self.user.get_username()

    def as_json(self):
        data = {}
        dct = self.user.__dict__
        keys_not_in = ['_state', 'password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined']
        for k in dct.keys():
            if dct[k] != None and k not in keys_not_in:
                if dct[k] != "":
                    data[k] = dct[k]
        data['registrated_at'] = str(self.registrated_at)
        data['verify_code'] = self.verify_code
        return data

