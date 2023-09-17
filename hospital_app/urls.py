from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('patients/<int:patient_id>/', views.patient_detail, name='patient-detail'),
    path('patients/', views.patient_list, name='patient-list'),
    path('patients/register/', views.patient_registration, name='patient-registration'),
    path('', views.main_dashboard, name='main-dashboard'),
    path('online-patients/', views.online_patients, name='online-patients'),  
    path('book-appointment/', views.book_appointment, name='book-appointment'), 
    path('search/', views.search_patient, name='search-patient'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('pass-reset/', auth_views.PasswordResetView.as_view(), name='pass-reset'),
    
    # Define similar URL patterns for doctors and appointments
]
