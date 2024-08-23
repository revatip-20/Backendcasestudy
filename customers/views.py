from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.contrib.auth.decorators import login_required

@login_required
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user
            service_request.save()
            return redirect('request_tracking')
    else:
        form = ServiceRequestForm()
    return render(request, 'customers/service_request_form.html', {'form': form})

@login_required
def request_tracking(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'customers/request_tracking.html', {'requests': requests})

@login_required
def account_info(request):
    return render(request, 'customers/account_info.html')

def tracking_home(request):
    return render(request, 'customers/tracking/tracking_home.html')

