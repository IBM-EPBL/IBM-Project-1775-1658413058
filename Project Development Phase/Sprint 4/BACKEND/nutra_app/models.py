from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from nutra import settings
from datetime import date

from rest_framework.authtoken.models import Token

# Create your models here.



class CustomUser(AbstractUser):
    user_type_choices = ((1,'Admin'),(2,'Developer'),(3,'ApiUsers'))
    user_type = models.CharField(default=1, max_length=20, choices=user_type_choices)


class AdminUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.PROTECT, default='')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.admin.username



class DeveloperUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.PROTECT, default='')
    auth_token = models.TextField()
    verify_token = models.TextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.admin.username





class ApiUsersUser(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.PROTECT, default='')
    auth_token = models.TextField()
    verify_token = models.TextField()
    req_per_day = models.IntegerField(default=100)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.admin.username


class Food(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    fdc_id = models.IntegerField(blank=False)
    food_class = models.CharField(max_length=255, default="", blank=True)
    data_type = models.CharField(max_length=255, default="", blank=True)
    description = models.TextField(default="",blank=True)
    food_category_id = models.IntegerField(default=0, blank=True)
    publication_date = models.DateField(blank=True, default="")
    scientific_name = models.CharField(max_length=255, default="", blank=True)
    food_key = models.CharField(max_length=255, default="", blank=True)
    is_having_nutrient_id = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,blank=True)
    updated_by = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.fdc_id)


class FoodCalorieConversionFactor(models.Model):
    id = models.AutoField(primary_key=True)
    food_nutrient_conversion_factor_id = models.IntegerField(default=0, blank=True)
    protein_value = models.FloatField(blank=True)
    fat_value = models.FloatField(blank=True)
    carbohydrate_value = models.FloatField(blank=True)
    calories = models.FloatField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.food_nutrient_conversion_factor_id)


class FoodCategory(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.IntegerField(default=0, blank=True)
    description = models.TextField(default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.description


class FoodNutrientConversionFactor(models.Model):
    id = models.AutoField(primary_key=True)
    food_nutrient_conversion_factor_id = models.IntegerField(blank=True)
    fdc_id = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.fdc_id)

class FoodProtienConversionFactor(models.Model):
    id = models.AutoField(primary_key=True)
    food_nutrient_conversion_factor_id = models.IntegerField(blank=True)
    value = models.IntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=255, blank=True)
    objects = models.Manager()
    
    def __str__(self):
        return str(self.food_nutrient_conversion_factor_id)


class FoodUpdateLogEntry(models.Model):
    id = models.AutoField(primary_key=True)
    fdc_id = models.IntegerField(blank=True)
    description = models.TextField(default="", blank=True)
    last_updated = models.DateField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.fdc_id)


class MeasureUnit(models.Model):
    id = models.AutoField(primary_key=True)
    measure_unit_id = models.IntegerField(blank=True)
    name = models.CharField(max_length=30, default='', blank=True)
    abbreviation = models.CharField(max_length=20, default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Nutrient(models.Model):
    id = models.AutoField(primary_key=True)
    nutrient_id = models.IntegerField(blank=True)
    name = models.CharField(max_length=30, default='', blank=True)
    unit_name = models.CharField(max_length=10, default='', blank=True)
    nutrient_nbr = models.IntegerField(blank=True, unique=True)
    rank = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.name


class NutrientIncomingName(models.Model):
    id = models.AutoField(primary_key=True)
    nutrient_incoming_name_id = models.IntegerField(blank=True)
    name = models.CharField(max_length=50, default='', blank=True)
    nutrient_id = models.IntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=255, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.name



def fruit_upload_location(instance, filename, **kwargs):
    return f'classifier/{str(instance.user.id)}/{date.today()}-{filename}'


class FruitClassifier(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, default='', on_delete=models.PROTECT)
    image = models.ImageField(upload_to=fruit_upload_location, null=False, blank=False)
    model_predicted_output = models.CharField(max_length=255, default='', blank=True)
    human_predicted_output = models.CharField(max_length=255, default='', blank=True)
    is_predicted_by_model_and_human_are_same = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=255, default='', blank=True)
    objects = models.Manager()


    def __str__(self):
        return self.model_predicted_output



def report_upload_location(instance, filename, **kwargs):
    return f'reports/{str(instance.user.id)}/{date.today()}-{filename}'


class Report(models.Model):
    id = models.AutoField(primary_key=True)
    # user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, blank=True, null=True)
    title = models.CharField(max_length=100, default='', blank=False)
    description = models.TextField()
    file = models.FileField(upload_to=report_upload_location, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.title



class MotivationalQuotes(models.Model):
    id = models.AutoField(primary_key=True)
    quote = models.CharField(max_length=200, default='', blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.quote


class UserDailyDetails(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    calories_morning = models.FloatField(default=0.0)
    calories_afternoon = models.FloatField(default=0.0)
    calories_night = models.FloatField(default=0.0)
    calories_today_total = models.FloatField(default=0.0)
    calories_previous_day = models.FloatField(default=0.0)
    objects = models.Manager()

    def __str__(self):
        return self.user.username



class BMICalculator(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.IntegerField(default=0)
    height_m = models.FloatField(default=0.0)
    weight_kg = models.FloatField(default=0.0)
    bmi = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.user.username}--{self.bmi}'



class UserFeedback(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300, default='', blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.title








@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if not created:
        return
    if instance.user_type == 1:
        AdminUser.objects.create(admin=instance)
    if instance.user_type == 2:
        DeveloperUser.objects.create(admin=instance)
    if instance.user_type == 3:
        ApiUsersUser.objects.create(admin=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminuser.save()
    if instance.user_type == 2:
        instance.developeruser.save()
    if instance.user_type == 3:
        instance.apiusersuser.save()
        


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        UserDailyDetails.objects.create(user=instance)



















