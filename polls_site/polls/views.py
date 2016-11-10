from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
# Another way to serialize data into xml or json
# from django.core import serializers

from .models import Question, Choice

# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {
		'latest_question_list': latest_question_list,
	}
	return render(request, 'index.html', context)

# JsonResponse Test
def jsonout(request):
	question = Question.objects.all().values('question_text', 'pub_date')
	question_list = list(question)
	return JsonResponse(question_list, safe=False)
	# data = serializers.serialize("xml", Question.objects.all())
	# return JsonResponse(data, safe=False)

def detail(request, question_id):
	question = get_obddject_or_404(Question, pk=question_id)
	context = {
		'question': question,
	}
	return render(request, 'detail.html', context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)