from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request , 'about/about-us.html')

def contact(request):
    return render(request , 'about/contact-us.html')