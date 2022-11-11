from rest_framework import serializers
from nutra_app.models import CustomUser, FruitClassifier, Food, FoodCalorieConversionFactor, Report, UserDailyDetails, MotivationalQuotes



class RegisterApiUsersUser(serializers.ModelSerializer):

    password_2 = serializers.CharField(style={'input_type':'password_2'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email','username','password','password_2','user_type']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def save(self):
        api_user = CustomUser(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            user_type = 3
        )

        password = self.validated_data['password']
        password_2 = self.validated_data['password_2']

        if password != password_2:
            raise serializers.ValidationError({'password':'Password must match'})
        api_user.set_password(password)
        api_user.save()
        return api_user



class FruitClassifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = FruitClassifier
        fields = ['id','image','model_predicted_output']



class FoodDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id','data_type','description']


class CalorieDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCalorieConversionFactor
        fields = ['protein_value','fat_value','carbohydrate_value','calories']



class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['title','description','file']


class UserDailyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDailyDetails
        fields = ['calories_morning','calories_afternoon','calories_night','calories_today_total','calories_previous_day']

class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotivationalQuotes
        fields = ['quote','description']






