#
from django.db import models

#
from .user_model import UserModel

class TodoModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    text = models.TextField(default='', blank=True, null=True)
    is_active = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return "User: {}\n Text: {}\nIs Active: {}"\
            .format(self.user.user.get_username, self.text, self.is_active)

    def as_json(self):
        data = {}
        data['user'] = self.user.as_json()
        data['text'] = self.text
        data['is_active'] = self.is_active
        return data
