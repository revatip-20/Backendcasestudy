from django.shortcuts import render, get_object_or_404
from customers.models import ServiceRequest
from django.contrib.auth.decorators import login_required

@login_required
def manage_requests(request):
    requests = ServiceRequest.objects.all().order_by('-created_at')
    return render(request, 'support/manage_requests.html', {'requests': requests})

@login_required
def request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    return render(request, 'support/request_detail.html', {'service_request': service_request})
