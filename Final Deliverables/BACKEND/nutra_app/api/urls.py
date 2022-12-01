from django.urls import path
from . import views


app_name = 'aira_app'



urlpatterns = [
    path('register-api-user/', views.register_api_user, name='register-api-user'),
    path('fruit-classifier/',views.predict_fruit_api, name='fruit-classifier-api'),
    path('search-fruits/',views.SearchFruit.as_view(), name='search-fruit'),
    path('fruit-detail/<int:id>/',views.food_data_api, name='fruit-details'),
    path('calorie-detail/<int:id>/',views.calories_data_api, name='calorie-detail'),
    path('user-daily-details',views.user_daily_details, name='user-daily-details'),
    path('search-quote',views.SearchQuote.as_view(), name='search-quote'),
    path('report',views.report, name='report'),
    path('bmi',views.bmi_calculator, name='bmi-calculator'),
    path('feedback',views.user_feedback, name='user-feedback'),
]





