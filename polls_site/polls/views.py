from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	context = {

	}
	return render(request, 'base.html', context)

def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)