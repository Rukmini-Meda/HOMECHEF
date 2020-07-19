from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'Paypal')
)

class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': "1234 Main St",
            'class': "form-control"
            
        }
    ))
    apartment_address = forms.CharField(required=False,widget=forms.TextInput(
        attrs={
            'placeholder': "Apartment or House",
            'class': "form-control"
        }
    ))
    country = CountryField(blank_label='(select country)').formfield(
        widget=CountrySelectWidget(
            attrs={
                'class': "custom-select d-block w-100",
                'id': "country"
            }
        )
    )
    zipfield = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': "form-control"
            }
        )
    )
    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={
            'class':"custom-control-input",
            'id':"same-address"
        }
    ),required=False)
    save_info = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={
            'class':"custom-control-input",
            'id':"save-info"
        }
    ),required=False)
    payment_option = forms.ChoiceField(widget=forms.RadioSelect,choices=PAYMENT_CHOICES)

