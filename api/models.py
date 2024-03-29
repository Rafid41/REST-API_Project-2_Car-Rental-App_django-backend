# api\models.py
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
import uuid

# Create your models here.
# custom User model process


# manager power dey ORM ba base model use korar
class UserManager(BaseUserManager):
    # ei create_user call hbe jokhon kono user / superuser create kri
    def create_user(self, email, password, account_type):
        if not email:
            raise ValueError("Please insert user Email")

        # normalize email: jemon uppercase / lowercase jhamela thake ta resolve kore
        email = self.normalize_email(email)

        # current model er under e user
        user = self.model(email=email, account_type=account_type)

        # encrypt password
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    # login to admin panel
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    # New field
    # account_type e choice field na dileo hoto, cz data receive hbe rest_api theke
    account_type = models.CharField(
        max_length=10,
        blank=True,
        choices=(
            ("Owner", "Owner"),
            ("Client", "Client"),
        ),
    )

    # manager er name
    objects = UserManager()
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email


########################## car page #######################
class Categories(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Cars(models.Model):
    car_name = models.CharField(max_length=200)
    car_number = models.CharField(max_length=100)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="owner_account"
    )

    car_category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    # time will be handled by react, it will only store the milliseconds
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)

    def get_unique_filename(instance, filename):
        # Generate a unique filename using UUID
        ext = filename.split(".")[-1]
        unique_id = uuid.uuid4().hex
        return f"car_photos/{unique_id}.{ext}"

    car_photo = models.ImageField(upload_to=get_unique_filename, null=True, blank=True)

    def __str__(self):
        return self.car_name


class CarBookingDate(models.Model):
    car_id = models.ForeignKey(Cars, on_delete=models.CASCADE, blank=True, null=True)
    booking_date = models.CharField(blank=True, null=True, max_length=20)
    booker_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="booker_account",
    )

    def __str__(self):
        return self.car_id.car_name + " | " + self.booking_date
