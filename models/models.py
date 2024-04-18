from django.db import models
from django.core.exceptions import ValidationError
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator

class User(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    telegram_id = models.SlugField(unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    tg_full_name = models.CharField(max_length=120)
    tg_username = models.CharField(max_length=120, null=True, blank=True)
    region = models.CharField(max_length=120)
    district = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=13)

    math_score = models.IntegerField(null=True, blank=True)
    iq_score = models.IntegerField(null=True, blank=True)
    english_score = models.IntegerField(null=True, blank=True)
    total_score = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0),
                                       MaxValueValidator(100)])

    create_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_ban = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    objects = models.Manager()


    def __str__(self):
        return self.first_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['-total_score']