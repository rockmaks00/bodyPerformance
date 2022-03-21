import datetime as datetime
from django.db import models
import urllib3
import json
from django.contrib.auth.models import User
from datetime import datetime
from project.settings import AZURE_URL, AZURE_APIKEY


class Body(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=datetime.now, blank=True)
    age = models.FloatField('age')
    gender = models.FloatField('gender')  # 0 - male; 1 - female
    height_cm = models.FloatField('height_cm')
    weight_kg = models.FloatField('weight_kg')
    fat = models.FloatField('fat')
    diastolic = models.FloatField('diastolic')
    systolic = models.FloatField('systolic')
    gripForce = models.FloatField('gripForce')
    sit_and_bend = models.FloatField('sit_and_bend')
    situps = models.FloatField('situps')
    jump_cm = models.FloatField('jump_cm')
    body_class = models.FloatField('body_class')  # 1 - A (perfect) ... 4 - C (bad)

    def get_class(self):
        data = {
            "Inputs": {
                "input1":
                    {
                        "ColumnNames": ["age", "gender", "height_cm", "weight_kg", "fat", "diastolic", "systolic",
                                        "gripForce", "sit_and_bend", "situps", "jump_cm", "body_class"],
                        "Values": [[self.age, self.gender, self.height_cm, self.weight_kg, self.fat, self.diastolic,
                                    self.systolic, self.gripForce, self.sit_and_bend, self.situps, self.jump_cm, 0],
                                   [self.age, self.gender, self.height_cm, self.weight_kg, self.fat, self.diastolic,
                                    self.systolic, self.gripForce, self.sit_and_bend, self.situps, self.jump_cm, 0] ]
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