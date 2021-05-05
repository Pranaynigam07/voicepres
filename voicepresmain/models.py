from django.db import models

# Create your models here.
class Register(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class Patient_Details(models.Model):
    case_id=models.CharField(max_length=20,primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    date=models.DateTimeField(auto_now_add=True)
    Symptoms=models.TextField()
    problem=models.TextField()
    status_choice=[("Pending","Pending"),("Closed","Closed")]
    case_status=models.CharField(max_length=10,choices=status_choice,default="Pending")

class Doctor_Table(models.Model):
    case_id=models.CharField(max_length=20,primary_key=True)
    name=models.CharField(max_length=100)
    Diagnosis=models.TextField()
    Prescription=models.TextField()
    Advice=models.TextField()

