from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'person/home.html')

def contact(request):
	return render(request, 'person/basic.html', {'con':('Contact me here:', 'hardeepsinghmehradoodle@gmail.com')})
