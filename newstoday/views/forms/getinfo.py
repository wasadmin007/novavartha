from django import forms
from newstoday.models.getcountries import getcountries 

import logging
logger = logging.getLogger(__name__)
class getinfoForm(forms.Form):
       
        country = forms.CharField(label='country', widget=forms.Select(choices=getcountries().getcountries()), initial='india')
        language = forms.CharField(label='language', widget=forms.Select(choices=getcountries().getlanguagech('india')))

