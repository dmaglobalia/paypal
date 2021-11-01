from django.shortcuts import render

# Create your views here.

def paymment(request):
    return render(request,'pay/main.html')