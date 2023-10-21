from django import forms

import datetime

class EventForm(forms.Form):

    def __init__(self, foo_choices, *args, **kwargs):
        self.base_fields['venue_id'].choices = foo_choices
        super(EventForm, self).__init__(*args, **kwargs)

    name = forms.CharField(max_length = 200)
    name.widget.attrs.update({'class': 'form-control form-control-lg'})  
    
    description = forms.CharField(max_length = 200)
    description.widget.attrs.update({'class': 'form-control form-control-lg'})  

    start_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control ', 'type':'date'}))

    end_date = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control ', 'type':'date'}))

    capacity = forms.IntegerField()
    capacity.widget.attrs.update({'class': 'form-control form-control-lg'})  

    venue_id = forms.ChoiceField(choices=(),required=True)
    venue_id.widget.attrs.update({'class': 'form-control form-control-lg'})

    def clean(self):

        cleaned_data = super().clean()
        
        if cleaned_data.get("start_date") and cleaned_data.get("end_date"):
            arrival_date = cleaned_data.get("start_date")
            departure_date = cleaned_data.get("end_date")

            if arrival_date.date() < datetime.date.today():
                error_message = forms.ValidationError("start date should be after today's date")
                self.add_error('start_date', error_message)

            elif departure_date.date() <= arrival_date.date():
                error_message = forms.ValidationError("end date should be after start date")
                self.add_error('end_date', error_message)

        return cleaned_data
    


class VenueForm(forms.Form):

    name = forms.CharField(max_length = 200)
    name.widget.attrs.update({'class': 'form-control form-control-lg'})  
    
    capacity = forms.IntegerField()
    capacity.widget.attrs.update({'class': 'form-control form-control-lg'})  

    latitude = forms.FloatField()
    latitude.widget.attrs.update({'class': 'form-control form-control-lg'})  

    longitude = forms.FloatField()
    longitude.widget.attrs.update({'class': 'form-control form-control-lg'})