from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
from datetime import date
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, logout
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse

from .models import CustomUser, FruitClassifier
from .api.serializers import RegisterApiUsersUser, FruitClassifierSerializer
from .ai_models import fruit
from .authentication import AuthBackEnd


# Create your views here.






@csrf_exempt
def predict_fruit(request):
    if request.method != 'POST':
        return HttpResponse('You are not allowed to do this')
    user = CustomUser.objects.get(id=request.user.id) if request.user.is_authenticated else CustomUser.objects.all().first()
    image = request.FILES['image']
    fs = FileSystemStorage()
    filename = fs.save(f'classifier/{str(request.user)}/{date.today()}-{image.name}', image)
    image_url = fs.url(filename)
    if request.method == 'POST':
        fruit_obj = FruitClassifier(user=user, image=image_url)
        fruit_obj.save()
        image = fruit_obj.image
        predicted_output = fruit.predict_fruit(image)
        fruit_obj.model_predicted_output = predicted_output
        fruit_obj = FruitClassifier.objects.get(id=fruit_obj.id)
        fruit_obj.model_predicted_output = predicted_output
        fruit_obj.save()
        return JsonResponse({'output':fruit_obj.model_predicted_output})


def login_user(request):
    if request.method != "POST":
        return HttpResponse('You are not allowed to do this')
    user = AuthBackEnd.authenticate(request, login_id=request.POST.get('LoginID'), password=request.POST.get('password'))
    if user != None:
        login(request, user)



def logout_user(request):
    logout(request)
    messages.success(request," Logout Successfully! ")
    return HttpResponseRedirect(reverse("show_login"))

































