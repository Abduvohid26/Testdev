import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator, MaxValueValidator
from .utils import validate_file_size
import random

class User(AbstractUser):
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE')
    )
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid.uuid4)
    phone_number = models.CharField(max_length=13, verbose_name='Phone Number')
    affiliation = models.CharField(max_length=100, verbose_name='Affiliation')
    country = models.CharField(max_length=500, verbose_name='Country')
    gender = models.CharField(max_length=100, choices=GENDER, default='MALE' , verbose_name='Gender')
    email = models.EmailField(unique=True, verbose_name='Email')

    def __str__(self) -> str:
        return f'{self.email}'
    
    def check_username(self):
        if not self.username:
            temp_username = f'test-{uuid.uuid4().__str__().split("-")[-1]}'
            while User.objects.filter(username=temp_username):
                temp_username = f'{temp_username}{random.randint(0, 9)}'
            self.username = temp_username

    
    def check_hash_password(self):
        if not self.password.startswith('pbkdf2_sha256'):
            self.set_password(self.password)

        
    def save(self, *args, **kwargs):
        self.check_username()
        self.check_hash_password()
        super(User, self).save(*args, **kwargs)


class PaperInformation(models.Model):
    id = models.UUIDField(unique=True, editable=False, primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255)
    key_words = models.IntegerField(validators=[MaxValueValidator(5)])
    section = models.CharField(max_length=255)
    file = models.FileField(upload_to='users/sections/',
        validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx']), validate_file_size])
    

    def __str__(self) -> str:
        return f'{self.title}'