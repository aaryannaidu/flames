from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import FlamesResult
# Create your views here.
class FlamesForm(forms.Form):
    name1 = forms.CharField(label="Name 1", widget=forms.TextInput(attrs={'placeholder': 'Enter first name'}))
    name2 = forms.CharField(label="Name 2", widget=forms.TextInput(attrs={'placeholder': 'Enter second name'}))



def game(request):
    result=''
    if request.method=='POST':
        form=FlamesForm(request.POST)
        if form.is_valid():


            name1 = form.cleaned_data["name1"].lower().replace(" ", "")
            name2 = form.cleaned_data["name2"].lower().replace(" ", "")
            
            for letter in name1:
                if letter in name2:
                    name1=name1.replace(letter,"",1)
                    name2=name2.replace(letter,"",1)
            count=len(name1)+len(name2)
            flames = ["Friends👀", "Love😍", "Affection😌", "Marriage💍", "Enemy😠", "Sibling 😵‍💫"]
            while len(flames)>1:
                i= (count-1)%len(flames)
                flames.pop(i)
        
            result= flames[0]
            FlamesResult.objects.create(name1=form.cleaned_data['name1'], name2=form.cleaned_data['name2'], result=result)

    else:
        form=FlamesForm()
        
    return render(request,'game.html',{'form':form,'result':result})

        
        
    

