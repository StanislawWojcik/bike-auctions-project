from .models import Auction
from django.forms import ModelForm, DateInput
from django import forms
from django.core.validators import MinValueValidator

class AuctionForm(ModelForm):
    production_date = forms.DateField(widget=DateInput(
        format=('%d/%m/%Y'),
        attrs={
            'class': 'form-control',
            'placeholder': 'Select a date',
            'type': 'date', }
    ))
    class Meta:
        model = Auction
        fields = ['title', 'description', 'bike_type', 'production_date', 'color', 'gears', 'size', 'price', 'image']
        labels = {'title':'title',
                  'description':'description',
                  'bike_type':'bike type',
                  'color':'color',
                  'gears':'gears',
                  'size':'size',
                  'price':'price',
                  }

class AuctionSeachForm(ModelForm):
    production_date_start = forms.DateField(widget=DateInput(
                format=('%d/%m/%Y'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date',}
            ))
    production_date_end = forms.DateField(widget=DateInput(
                format=('%d/%m/%Y'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date',}
            ))
    gears_min = forms.IntegerField(min_value=0)
    gears_max = forms.IntegerField(min_value=0)
    price_min = forms.DecimalField(max_digits=9, decimal_places=2, validators=[MinValueValidator(0.00)])
    price_max = forms.DecimalField(max_digits=9, decimal_places=2, validators=[MinValueValidator(0.00)])
    class Meta:
        model = Auction
        label = {'Ordered': 'non available auctions'}
        exclude = ('description', 'owner', 'production_date', 'price', 'gears', 'user', 'ordered', 'image')

    def __init__(self, *args, **kwargs):
        super(AuctionSeachForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = False
        self.fields['color'].required = False
        self.fields['gears_min'].required = False
        self.fields['gears_max'].required = False
        self.fields['size'].required = False
        self.fields['bike_type'].required = False
        self.fields['production_date_end'].required = False
        self.fields['production_date_start'].required = False
        self.fields['price_min'].required = False
        self.fields['price_max'].required = False

    field_order = ['title', 'color', 'size', 'bike_type',
                   'gears_min', 'gears_max', 'production_date_start','production_date_end',
                   'price_min', 'price_max']
