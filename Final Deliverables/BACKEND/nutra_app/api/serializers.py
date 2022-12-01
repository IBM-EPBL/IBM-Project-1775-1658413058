from rest_framework import serializers

from nutra_app.models import (CustomUser, Food, FoodCalorieConversionFactor,
                              FruitClassifier, MotivationalQuotes, Report,
                              UserDailyDetails, BMICalculator, UserFeedback)


class RegisterApiUsersUser(serializers.ModelSerializer):

    password_2 = serializers.CharField(style={'input_type':'password_2'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username','password','password_2','user_type']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def save(self):
        # if self.validated_data['email'] == '':
        #     self.custom_data = 'email-error'
        #     return self
        if self.validated_data['username'] == '':
            self.custom_data = 'username-error'
            return self
        if self.validated_data['password'] == '':
            self.custom_data = 'password-error'
            return self
        if self.validated_data['password_2'] == '':
            self.custom_data = 'password_2-error'
            return self
        if self.validated_data['password'] != self.validated_data['password_2']:
            self.custom_data = 'password-match-error'
            return self
        api_user = CustomUser(
            email = 'no_email@gmail.com',
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




class BMICalculatorSerializer(serializers.ModelSerializer):
    user = serializers.RelatedField(source='CustomUser', read_only=True)
    class Meta:
        model = BMICalculator
        fields = ['user','height_m','weight_kg','bmi']

        def save(self):
            height = float(self.validated_data['height'])
            weight = float(self.validated_data['weight'])
            num = weight
            denom = height**2
            bmi_cal = num/denom
            
            bmi_data = BMICalculator(
                height_m = height,
                weight_kg = weight,
                bmi = bmi_cal
            )
            
            bmi_data.save()
            return self



class UserFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFeedback
        fields = ['title','description']











