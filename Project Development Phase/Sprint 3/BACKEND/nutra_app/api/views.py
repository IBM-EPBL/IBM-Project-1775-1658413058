from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from nutra.settings import BASE_DIR
from nutra_app.ai_models import fruit
from nutra_app.models import (BMICalculator, CustomUser, Food,
                              FoodCalorieConversionFactor,
                              FoodNutrientConversionFactor, FruitClassifier,
                              MotivationalQuotes, UserFeedback)

from .serializers import (CalorieDataSerializer, FoodDataSerializer,
                          FruitClassifierSerializer, QuotesSerializer,
                          RegisterApiUsersUser, ReportSerializer,
                          UserDailyDetailsSerializer, BMICalculatorSerializer, UserFeedbackSerializer)


@api_view(['POST'])
def register_api_user(request):

    serializer = RegisterApiUsersUser(data=request.data)
    data = {}
    Response.status_code = 400
    # if request.data['email'] == '':
    #     return Response({'error':'Please provide email details'})
    if request.data['username'] == '':
        return Response({'error':'Please provide username details'})
    if request.data['password'] == '':
        return Response({'error':'Please provide password details'})
    if request.data['password_2'] == '':
        return Response({'error':'Please provide password_2 details'})
    if request.data['password'] != request.data['password_2']:
        return Response({'error':'Password and Conform Password must match'})
    temp_name = request.data['username']
    try:
        if CustomUser.objects.get(username=temp_name):
            return Response({'error':'User already exists'})
    except Exception:
        if serializer.is_valid():
            Response.status_code = 200
            account = serializer.save()
            
            height = request.data['height']
            weight = request.data['weight']
            bmi = height/weight **2
            bmi_obj = BMICalculator(
                height_m = height,
                weight_kg = weight,
                bmi = bmi,
                user = account.id
            ) 
            bmi_obj.save()

            # data['email'] = account.email
            data['username'] = account.username
            data['response'] = 'Successfully registered a new Public User'
            return Response(data)

    
    



@api_view(['POST'])
def predict_fruit_api(request):
    
    user = CustomUser.objects.get(id=request.user.id)
    image_model = FruitClassifier(user=user)

    if request.method == 'POST':
        serializer_data = FruitClassifierSerializer(image_model, data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            image = serializer_data.data['image']
            predicted_output = fruit.predict_fruit(image)
            serializer_data._data['model_predicted_output'] = predicted_output
            fruit_obj = FruitClassifier.objects.get(id=serializer_data.data['id'])
            fruit_obj.model_predicted_output = predicted_output
            fruit_obj.save()
            return Response(serializer_data.data, status=status.HTTP_201_CREATED)
        return Response(serializer_data.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
# @permission_classes((IsAuthenticated,))
def food_data_api(request,id):

    try:
        food_obj = Food.objects.get(id=id)
    except Food.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    serializer = FoodDataSerializer(food_obj)
    return Response(serializer.data)



@api_view(['GET'])
# @permission_classes((IsAuthenticated,))
def calories_data_api(request,id):

    try:
        fdc_id = Food.objects.get(id=id).fdc_id
        try:
            nutrient_id = FoodNutrientConversionFactor.objects.filter(fdc_id=fdc_id).first().food_nutrient_conversion_factor_id
        except FoodNutrientConversionFactor.DoesNotExist:
            return Response({'nutrient data not available'})
        
        try:
            calorie_obj = FoodCalorieConversionFactor.objects.filter(food_nutrient_conversion_factor_id=nutrient_id).first()
        except FoodCalorieConversionFactor.DoesNotExist:
            return Response('calorie data not available')
        
    except Food.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    serializer = CalorieDataSerializer(calorie_obj)
    return Response(serializer.data)



@api_view(['POST'])
def report(request):
    report = ReportSerializer(data=request.data)
    if report.is_valid():
        report.save()
        return Response("Sorry for the inconvenience you faced in our application. We will look into your report and if it's valid, we will try to solve it as soon as possible.")
    return Response('Please provide necessary informations to report')



    
@api_view(['POST','GET'])
def user_daily_details(request):
    if request.method == 'POST':
        serializer = UserDailyDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('SUCCESS')
    elif request.method == 'GET':
        data = user_daily_details.objects.get(id=request.user.id)
        return Response(data)
        


@api_view(['POST','GET'])
def bmi_calculator(request):
    if request.method == 'GET':
        data = BMICalculator.objects.get(user=request.user)
        return Response({'bmi':data})
    elif request.method == 'POST':
        height = float(request.data['height'])
        weight = float(request.data['weight'])
        num = weight
        denom = height**2 
        bmi_cal = num/denom
        bmi_obj = BMICalculator(
            height_m=height,
            weight_kg=weight,
            bmi=bmi_cal,
            user=request.user.id
        )
        bmi_obj.save()
        out = {
            'height':height,
            'weight':weight,
            'bmi':bmi_cal
        }
        return Response(out)




@api_view(['POST'])
def user_feedback(request):
    if request.method != 'POST':
        return Response('You are allowed to do this. Please Contact Administrator')
    serializer = UserFeedbackSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



class SearchFruit(ListAPIView):
    queryset = Food.objects.filter(is_having_nutrient_id=1)
    serializer_class = FoodDataSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('data_type','description')


class SearchQuote(ListAPIView):
    queryset = MotivationalQuotes.objects.all()
    serializer_class = QuotesSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,)
    search_fields = ('quote','description')






