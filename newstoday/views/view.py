from django.shortcuts import render
from django.template.defaulttags import register
from django.http.response import HttpResponse
from newstoday.apps.getlatestnews import getappnews

#class AutoCompleteZones():#autocomplete.Select2QuerySetView):
#	def autocompletezones():
#		zones = data().get_avalable_zones('us-east-1')
#		return zones
def title():
    return 'News ToDay'

def template(request):
    fileTemp = 'index.html'
    return render(request,fileTemp, {'formset': 'News Today' , 'Tabs': 'data().data_static()' ,'title':title()})
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
