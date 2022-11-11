from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from nutra.settings import BASE_DIR
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

from nutra_app.models import CustomUser, FruitClassifier, Food, FoodNutrientConversionFactor, FoodCalorieConversionFactor, MotivationalQuotes
from .serializers import RegisterApiUsersUser, FruitClassifierSerializer, FoodDataSerializer, CalorieDataSerializer, ReportSerializer, QuotesSerializer, UserDailyDetailsSerializer
from nutra_app.ai_models import fruit






@api_view(['POST'])
def register_api_user(request):

    serializer = RegisterApiUsersUser(data=request.data)
    data = {}

    if serializer.is_valid():
        account = serializer.save()
        data['response'] = 'Successfully registered a new Public User'
        data['email'] = account.email
        data['username'] = account.username
        # data['token'] = Token.objects.get(user=account).key
    else:
        data = serializer.errors
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






