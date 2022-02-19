from django.shortcuts import render
from .models import Body


def index(request):
    return render(request, 'index.html')


def calculate(request):
    return render(request, 'calculate.html')


def result(request):
    body_data = Body(request.GET['age'], request.GET['gender'], request.GET['height_cm'], request.GET['weight_kg'],
                    request.GET['fat'], request.GET['diastolic'], request.GET['systolic'], request.GET['gripForce'],
                    request.GET['sit_and_bend'], request.GET['situps'], request.GET['jump_cm'])
    body_data.body_class = body_data.get_class()
    return render(request, 'result.html')
