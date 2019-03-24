from django.db import models
from datetime import datetime
# Create your models here.
class SinhVien(models.Model):
    name = models.CharField(max_length=100)
    msv = models.CharField(max_length=20)
    lop = models.TextField()
    ngaysinh = models.DateField(default=datetime.now)


