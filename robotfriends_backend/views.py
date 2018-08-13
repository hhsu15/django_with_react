from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse


# Create your views here.
# def index(request):
# 	return HttpResponse("Hello World")
def index(request):
	return render(request, "index.html")

def test(request):
	return HttpResponse("Hello World. This is a test")
	
def get_data(request):
	api_data = {'name':'Hsin'}
	return JsonResponse(api_data)

def send_data(request):
	print('data is saved in db')
	return HttpResponse("Your data has been saved")

def search_robot(request, robot_name):
	return render(request, "index.html", {'robot_name':robot_name})



