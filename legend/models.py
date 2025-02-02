from django.db import models

# Create your models here.
from django.db import models

class FlamesResult(models.Model):
    name1 = models.CharField(max_length=100)
    name2 = models.CharField(max_length=100)
    result = models.CharField(max_length=20)
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request 

    def __str__(self):
        return f"{self.name1} & {self.name2} → {self.result}"
