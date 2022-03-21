from django.core import serializers
from django.shortcuts import render, redirect
from .models import Body
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def login(request):
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def index(request):
    print(request.user.first_name)
    return render(request, 'index.html', {'username': f'{request.user.first_name} {request.user.last_name}'})


@login_required(login_url='/login/')
def calculate(request):
    return render(request, 'calculate.html')


@login_required(login_url='/login/')
def result(request):
    body_data = Body(
        author=User.objects.get(id=request.user.id),
        age=request.GET['age'], gender=request.GET['gender'], height_cm=request.GET['height_cm'],
        weight_kg=request.GET['weight_kg'],
        fat=request.GET['fat'], diastolic=request.GET['diastolic'], systolic=request.GET['systolic'],
        gripForce=request.GET['gripForce'],
        sit_and_bend=request.GET['sit_and_bend'], situps=request.GET['situps'],
        jump_cm=request.GET['jump_cm'])
    body_data.body_class = body_data.get_class()
    body_data.save()
    return render(request, 'result.html', {'result': body_data})


@login_required(login_url='/login/')
def profile(request):
    data = Body.objects.filter(author=request.user.id)
    return render(request, 'profile.html', {'data': data, 'data_json': serializers.serialize("json", data)})
