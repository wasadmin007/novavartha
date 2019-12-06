from django import forms

import logging
logger = logging.getLogger(__name__)
class jbossForm(forms.Form):
        languages = forms.CharField(label='languages', widget=forms.Select(choices=data().cloud_choices()))
        countries = forms.CharField(label='countries', widget=forms.Select(choices=data().get_avalable_regions_choices()), initial='us-east-1')
        class Meta:
           model = data().get_avalable_regions_choices()
           fields = ( 'countries', 'languages')
