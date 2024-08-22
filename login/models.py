from django.db import models
from django.contrib.auth.models import UserManager

class CustomUser(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.EmailField(unique=True, max_length=765)
    username = models.CharField(max_length=765, blank=True)
    password = models.CharField(max_length=120)
    # external = models.IntegerField(null=True, blank=True)
    # purged = models.IntegerField(null=True, blank=True)
    # form_values_id = models.IntegerField(null=True, blank=True)
    # disk_usage = models.DecimalField(null=True, max_digits=16, decimal_places=0, blank=True)
    deleted = models.IntegerField(null=True, blank=True)
    create_time = models.DateTimeField(null=True, blank=True)
    update_time = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    is_anonymous = False
    is_authenticated = False

    class Meta:
        db_table = u'custom_user'