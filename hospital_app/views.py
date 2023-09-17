from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404,redirect,HttpResponse
from django.urls import reverse
from .models import Patient
from .forms import PatientForm  # You'll need to create a PatientForm
from .forms import AppointmentForm
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import user_passes_test


def notification(message,type):
# Assuming your form is valid
    notify_message = message
    notify_type=type
    online_patients = Patient.objects.filter(is_online=True)
    return {"notify_message":notify_message,"notify_type":notify_type,"online_patients":online_patients}

@login_required
def main_dashboard(request):
    # You can fetch data or perform other logic here

    '''View Perms'''
    from django.contrib.auth.models import User
    user = User.objects.get(username='omx')
    print()


    online_patients = Patient.objects.filter(is_online=True)
    return render(request, 'hospital_app/main_dashboard.html',{'online_patients': online_patients})

from django.contrib.auth import login, authenticate


def logout_view(request):
    logout(request)
    # Redirect to a page after logout (e.g., home page)
    return redirect('main-dashboard')

# Create a registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a login page or user dashboard
            return redirect('login-page')
    else:
        form = UserCreationForm()
    return render(request, 'hospital_app/register.html', {'form': form})



def toggle_online_status(request, patient_id):
    try:
        patient = Patient.objects.get(id=patient_id)
        patient.is_online = not patient.is_online
        patient.save()
        return JsonResponse({'status': 'success'})
    except Patient.DoesNotExist:
        return JsonResponse({'status': 'error'})
    
def has_permission(request,perm):
    has_permission = perm in request.user.get_group_permissions()
    return has_permission
    


#@user_passes_test(has_permission)
def book_appointment(request):

    if not has_permission(request,'hospital_app.add_appointment'):
        s=notification("No Enough perm","error")
        return render(request, 'hospital_app/main_dashboard.html',s)
    
    if request.method == 'POST':
        
        form = AppointmentForm(request.POST)
        manual_patient_id = request.POST.get('manual_patient_id')
        
        
        
        #print(manual_patient_id,id_patient)
        def success():
            
            # Check if the patient ID was manually entered
            
            try:
                print(manual_patient_id)
                if manual_patient_id:
                    # Check if the patient with this ID already exists
                    patient, created = Patient.objects.get_or_create(patient_id=manual_patient_id)
                    print(patient)
                    form.instance.patient = patient

            except:
                print("Error")
            # Save the appointment
            form.save()
            return True
    
            
        if form.is_valid():
            print("Form is valid")
            success()

            s=notification("Appointment has been booked","success")
            return render(request, 'hospital_app/main_dashboard.html',s)
            #return redirect('main-dashboard',)
    else:
        form = AppointmentForm()
        print("Error in form    ")

    return render(request, 'hospital_app/book_appointment.html', {'form': form})

def search_patient(request):
    if request.method == 'GET':
        patient_id = request.GET.get('patient_id', '')

        if patient_id:
            # Perform a database query to retrieve patient details by patient ID
            patient = get_object_or_404(Patient, patient_id=patient_id)
            return render(request, 'hospital_app/patient_detail.html', {'patient': patient})
        else:
            # Handle the case where no patient ID is provided
            return render(request, 'hospital_app/main_dashboard.html', {'error_message': 'Please enter a valid Patient ID.'})
    else:
        # Handle other HTTP methods if necessary
        return HttpResponseNotAllowed(['GET'])


def patient_registration(request):
    if not has_permission(request,'hospital_app.add_patient'):
        s=notification("No Enough perm","error")
        return render(request, 'hospital_app/main_dashboard.html',s)
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('patient-list')  # Redirect to the patient list after successful registration
        else:
            # Handle form validation errors if any
            # You can add error messages or additional handling here
            print("error")
    else:
        form = PatientForm()
    
    return render(request, 'hospital_app/patient_registration.html', {'form': form})


def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, patient_id=patient_id)
    return render(request, 'hospital_app/patient_detail.html', {'patient': patient})



def patient_list(request):
    patients = Patient.objects.all()  # Query to get all patients
    return render(request, 'hospital_app/patient_list.html', {'patients': patients})




def online_patients(request):
    online_patients = Patient.objects.filter(is_online=True)
    return render(request, 'hospital_app/online_patients.html', {'online_patients': online_patients})



