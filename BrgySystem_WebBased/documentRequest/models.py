from django.db import models
from accounts.models import User
import datetime

# Create your models here.
class docType(models.Model):
    Document_Choices = (
        ('Barangay Indigency','Barangay Indigency'),
        ('Barangay Clearance', 'Barangay Clearance'),
        ('Barangay Residency', 'Barangay Residency'),
    )
    Document_Type = models.CharField(max_length=100,choices=Document_Choices)
    is_Pending = models.BooleanField(default=True)
    is_Done = models.BooleanField(default=False)

    class Meta:
        abstract = True

class docRequest(docType):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    nationality = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    Address = models.CharField(max_length=255)
    email =  models.CharField(max_length=255)
    requested_by = models.ForeignKey(User,on_delete=models.CASCADE)
    requested_at = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.Document_Type
