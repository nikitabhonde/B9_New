from django import forms

from .models import Book  # 1st import your model(i.e Book) from .models

""" 2) forms.ModelForm """
""" path('form_view/', form_view, name="form_view") eske liye bhi yhi url use kiya hai"""
class BookForm(forms.ModelForm):
    # yaha or koi field add krni ho jo model mai present nhi hai to kr skte hai  
    class Meta:
        model = Book            # Jo model humne models.py mai create kiya hai 
        fields = ("__all__")      # all means book mdhe jya pn files asel te sb yenar name, price etc bt kahi selected pahije asel tr te apn tuple mdhe deu shakto
        exclude = ("is_active", )        # konti field nsel pahije tr apn exclude cha use kru shako



""" 3) crispy-forms :- Python package that styles the Django forms with the help of built-in template packs. """
""" This for Explanation purpose only not related to our Library-Project """
STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))    # attrs means attribute
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(label='Address',widget=forms.TextInput(attrs={'placeholder': '1234 Main St'}))
    address_2 = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'}))
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)


""" This for Explanation purpose only not related to our Library-Project """
""" 1) forms.Form """
""" path('form_view/', form_view, name="form_view") eske liye bhi yhi url use kiya hai"""
class Input_form(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)
    date_time = forms.DateTimeField(widget=forms.SelectDateWidget(years=range(2000,2031)))
    price = forms.IntegerField()
    is_active = forms.BooleanField()
    passworrd = forms.CharField(widget=forms.PasswordInput())
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    roll_number = forms.IntegerField(help_text="Enter 4 digit roll number")
    

    