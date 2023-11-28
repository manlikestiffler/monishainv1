from django.forms import ModelForm
from .models import *
from django import forms


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
class UpdateForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
class IssueForm(ModelForm):
    
    class Meta:
        model = Product
        fields = ('issue_to','issue_quantity')
        
class ReceiveForm(ModelForm):
	class Meta:
		model = Product
		fields = ['receive_quantity']
        
class ProductHistorySearchForm(forms.ModelForm):
	class Meta:
		model = ProductHistory
		fields =  '__all__'