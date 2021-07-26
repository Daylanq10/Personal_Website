from django.shortcuts import render


# Create your views here.
def homepage(request):
    # messages.info(request, "Logged out successfully")  # Doesnt work will figure out
    return render(request, 'Homepage.html')
