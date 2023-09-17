from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

# Create a custom user manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(email, first_name, last_name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    is_online = models.BooleanField(default=False)  # Add this field
    national_id = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()  # Add the email field here


    patient_id = models.CharField(max_length=15)

    def save(self, *args, **kwargs):
        if not self.patient_id:
            # Get the maximum patient_id value and increment it by 1
            last_patient = Patient.objects.order_by('-patient_id').first()
            if last_patient:
                # Increment the integer value and convert it to a string
                self.patient_id = str(int(last_patient.patient_id) + 1)
            else:
                # If no patients exist, start with 100000
                self.patient_id = '100000'

        super(Patient, self).save(*args, **kwargs)



    def __str__(self):
        return f"({self.patient_id}) {self.first_name} {self.last_name}"
    
class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email= models.EmailField()  # Add the email field here
    # Add more doctor information fields

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()  # Correct field name
    
    # Add more appointment-related fields

    def __str__(self):
        return "(Appointment: {}) {} {}".format(str(self.appointment_date).split("+")[0], self.patient, self.doctor)
