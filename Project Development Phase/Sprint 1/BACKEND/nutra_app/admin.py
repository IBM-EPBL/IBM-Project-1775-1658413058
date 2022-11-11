from django.contrib import admin

from nutra_app.models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(AdminUser)
admin.site.register(DeveloperUser)
admin.site.register(ApiUsersUser)
admin.site.register(FruitClassifier)
admin.site.register(Food)
admin.site.register(FoodCalorieConversionFactor)
admin.site.register(FoodCategory)
admin.site.register(FoodNutrientConversionFactor)
admin.site.register(FoodProtienConversionFactor)
admin.site.register(FoodUpdateLogEntry)
admin.site.register(MeasureUnit)
admin.site.register(Nutrient)
admin.site.register(NutrientIncomingName)
admin.site.register(Report)
admin.site.register(MotivationalQuotes)
admin.site.register(UserDailyDetails)









