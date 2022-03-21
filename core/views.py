from django.shortcuts import render
from .models import Body


def index(request):
    return render(request, 'index.html')


def calculate(request):
    return render(request, 'calculate.html')


def result(request):
    body_data = Body(age = request.GET['age'], gender = request.GET['gender'], height_cm = request.GET['height_cm'], weight_kg = request.GET['weight_kg'],
                    fat = request.GET['fat'], diastolic = request.GET['diastolic'], systolic = request.GET['systolic'], gripForce = request.GET['gripForce'],
                    sit_and_bend = request.GET['sit_and_bend'], situps = request.GET['situps'], jump_cm = request.GET['jump_cm'])
    body_data.body_class = body_data.get_class()
    return render(request, 'result.html', {'result': body_data})

