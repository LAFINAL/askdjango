from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    # user = models.OneToOneField(User) # FIXME: BAD case!! # user_id 라는 field가 생김.
    # import User에서 User가 변경되었을때 OneToOneField(User)의 User 값이 바뀌지 않아서 오류남.
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=50)