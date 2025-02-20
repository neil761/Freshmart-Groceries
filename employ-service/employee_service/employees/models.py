from django.db import models

class Employee(models.Model):
    fullname = models.CharField(max_length=255)
    dateofbirth = models.DateField()
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    emergency_contact_details = models.TextField()

    def __str__(self):
        return self.fullname