from django import forms
from game.models import question
from game.models import answer

class questionForm(forms.ModelForm):
	class Meta:
		model = question
		fields = '__all__'

class answerForm(forms.ModelForm):
	class Meta:
		model = answer
		fields = '__all__'