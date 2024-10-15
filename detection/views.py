# detection/views.py

from django.shortcuts import render
from .ml_models import predict_phishing  # Import your function for phishing detection

def home(request):
    if request.method == 'POST':
        url = request.POST.get('url', '')
        is_phishing = predict_phishing(url)
        return render(request, 'detection/home.html', {'url': url, 'is_phishing': is_phishing})
    return render(request, 'detection/home.html')

def url_detection(request):
    if request.method == 'POST':
        url = request.POST.get('url', '')
        is_phishing = predict_phishing(url)
        return render(request, 'detection/url_detection.html', {'url': url, 'is_phishing': is_phishing})
    return render(request, 'detection/url_detection.html')

# def image_detection(request):
#     # Implement image detection logic if required
#     return render(request, 'detection/image_detection.html')
