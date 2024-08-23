from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_service_request, name='submit_service_request'),
    path('tracking/', views.request_tracking, name='request_tracking'),
    path('account/', views.account_info, name='account_info'),
]
