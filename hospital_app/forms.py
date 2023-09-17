from django.utils import timezone
from django import forms
from .models import Doctor, Patient,Appointment

#from bootstrap_datepicker_plus import DateTimePickerInput  # Import the widget
#pip install django-bootstrap-datepicker-plus

class AppointmentForm(forms.ModelForm):
    manual_patient_id = forms.CharField(required=False)
  
    class Meta:
        

        model = Appointment
        fields = ['patient', 'doctor', 'appointment_date']
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'format': '%Y-%m-%dT%H:%M'})
            
        }

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        


        # Filter patient choices based on your condition (e.g., is_online=True)
        self.fields['patient'].queryset = Patient.objects.filter(is_online=True)

        # Set default value for appointment_date (e.g., current time)
        self.initial['appointment_date'] = timezone.now()


        # Check if a manual patient ID is provided
        manual_patient_id = self.data.get('manual_patient_id')
        
        # Disable the 'required' attribute for the patient field if manual_patient_id is provided
        if manual_patient_id!=None:
            self.fields['patient'].required = False
            self.fields['patient'].disabled = True
        else:
            self.fields['patient'].required = True
            self.fields['patient'].disabled = False


       

    # Your other form methods and validation here
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'date_of_birth', 'national_id', 'blood_type', 'phone_number', 'email']