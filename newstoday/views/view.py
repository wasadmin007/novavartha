from django.shortcuts import render
from django.template.defaulttags import register
from django.http.response import HttpResponse
from newstoday.apps.getlatestnews import getappnews
from newstoday.models.getcountries import getcountries
from newstoday.views.forms.getinfo import getinfoForm
from django.http import HttpResponseRedirect
#class AutoCompleteZones():#autocomplete.Select2QuerySetView):
#	def autocompletezones():
#		zones = data().get_avalable_zones('us-east-1')
#		return zones
def title():
    return 'News ToDay'

def template(request):
    fileTemp = 'index.html'
    countries = getcountries().getcountries()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        forms = getinfoForm(request.POST)
        # check whether it's valid:
        if forms.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
             return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        forms = getinfoForm()
    return render(request,fileTemp, {'formset': 'News Today', 'forms': forms,'countries': countries ,'title':title()})


def country(request):
    fileTemp = 'test.html'
    data = getcountries().getcountries()
    countries = getcountries().getcountries()
    return render(request, fileTemp, {'forms': countries})

def languages(request,country):
    fileTemp = 'languages.html'
    
    data = getcountries().getlanguages(country)
    str = ''
    for language in data:
       str+= language+' '
    data = str
    return render(request,fileTemp, {'formset': 'News Today' , 'languages': [data]} )
  
def latestnews(request,country,language):
    #country = request.GET.get('country')
    #language = request.GET.get('language')
    fileTemp = 'latestnews.html' 
    col = getappnews().getname(country,language) 
    data = getappnews().getdata((col))
     
    return render (request, fileTemp, { "data": data})
  

def awszones(request):
    region = request.GET.get('region')
    #region = 'us-east-1'
    fileTemp = 'awszones.tpl'
    #dat = list(data().get_avalable_zones_ax(region))
    return render(request,fileTemp, { 'zones': 'dat'})
    #return render(request,fileTemp, {'cities': zones})
def orderview(request):
    fileTemp = 'vieworder.tpl'
    return render(request,fileTemp, {'formset': 'Praveen Testting' , 'Tabs': 'data().data_static()' ,'title':title()})
