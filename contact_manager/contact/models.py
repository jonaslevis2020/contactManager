
from datetime import timezone
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.forms import forms, widgets
from django.utils.timezone import datetime, now
from django.db.models.fields import CharField, DateTimeField, EmailField, IntegerField
from django.db.models.fields.files import ImageField
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    manager = ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=50)
    email = EmailField(verbose_name='email',max_length=50)
    phone = IntegerField(blank=False, unique=True)
    info = CharField(blank=True, max_length=50)
    gender = CharField(max_length=10, choices=[('male','Male'),('female','Female')])
    image = ImageField(upload_to=('static/media/'), blank=True)
    date_added = DateTimeField(default=datetime.now)


    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-id'] #order contacts by descending id

class AppUser(models.Model):
    name = CharField(max_length=50)
    email = EmailField(max_length=50)
    password = models.CharField(widgets.PasswordInput, max_length=50)