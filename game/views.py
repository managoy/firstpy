from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from game.models import question
from game.forms import questionForm
from game.forms import answerForm


# Create your views here.
def home(request):
	ob = question.objects.all()
	context_dict = {'ob':ob}
	return render(request,'home.html',context_dict)
def welldone(request):
	ob = question.objects.all()
	context_dict = {'ob':ob}
	return render(request,'welldone.html',context_dict)
def incorrect(request):
	ob = question.objects.all()
	context_dict = {'ob':ob}
	return render(request,'incorrect.html',context_dict)

def fill_question(request):
	if request.method == 'POST':
		print(request.method,'===========================')
		forms = questionForm(request.POST,request.FILES)
		print(request.POST,'-----------------------------')
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/home/')
	else:
		forms = questionForm()
	context_dict= {'forms':forms}
	return render(request,'question.html',context_dict)

def fill_answer(request):
	if request.method == 'POST':
		print(request.method,'===========================')
		forms = answerForm(request.POST,request.FILES)
		print(request.POST,'-----------------------------')
		if forms.is_valid():
			forms.save()
		  
		p = question.objects.get(id=request.POST['q'])
		
		print(p)
		if(request.POST['a'].lower() == p.A.lower()):
		   	return HttpResponseRedirect('/welldone/')
		else:
			return HttpResponseRedirect('/incorrect/')


		# return HttpResponse(a)
	else:
		forms = answerForm()
	context_dict= {'forms':forms}
	return render(request,'answer.html',context_dict)
	