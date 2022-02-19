from django.db import models
import urllib3
import json
from bodyPerformance.settings import AZURE_URL, AZURE_APIKEY


class Body(models.model):
    age = models.FloatField('age')
    gender = models.CharField('gender')
    height_cm = models.FloatField('height_cm')
    weight_kg = models.FloatField('weight_kg')
    fat = models.FloatField('fat')
    diastolic = models.FloatField('diastolic')
    systolic = models.FloatField('systolic')
    gripForce = models.FloatField('gripForce')
    sit_and_bend = models.FloatField('sit_and_bend')
    situps = models.FloatField('situps')
    jump_cm = models.FloatField('jump_cm')
    body_class = models.CharField('body_class')

    def __init__(self, age, gender, height_cm, weight_kg, fat, diastolic, systolic, gripForce, sit_and_bend, situps,
                 jump_cm):
        self.age = age
        self.gender = gender
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.fat = fat
        self.diastolic = diastolic
        self.systolic = systolic
        self.gripForce = gripForce
        self.sit_and_bend = sit_and_bend
        self.situps = situps
        self.jump_cm = jump_cm

    def get_class(self):
        data = {
            "Inputs": {
                "input1":
                    {
                        "ColumnNames": ["age", "gender", "height_cm", "weight_kg", "fat", "diastolic", "systolic",
                                        "gripForce", "sit_and_bend", "situps", "jump_cm", "body_class"],
                        "Values": [[self.age, self.gender, self.height_cm, self.weight_kg, self.fat, self.diastolic,
                                    self.systolic, self.gripForce, self.sit_and_bend, self.situps, self.jump_cm],
                                   [self.age, self.gender, self.height_cm, self.weight_kg, self.fat, self.diastolic,
                                    self.systolic, self.gripForce, self.sit_and_bend, self.situps, self.jump_cm], ]
                    }, },
            "GlobalParameters": {
            }
        }

        body = str.encode(json.dumps(data))
        headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + AZURE_APIKEY)}
        http = urllib3.PoolManager()
        req = http.request('POST', url=AZURE_URL, body=body, headers=headers)
        result = json.loads(req.data.decode('utf-8'))

        return result['Results']['output1']['value']['Values'][0][-1]
