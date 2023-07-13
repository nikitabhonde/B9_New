from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User

""" User model by-define avaliable hota hai, yaha pe 'from django.contrib.auth.models import User' """
""" django.contrib.auth.models mai 2 models avaliable hote hai 1)User 2)Group """

# # We define one class i.e NewUserForm & UserCreationForm ko usme inherit kiya hai so use his properties
""" UserCreationForm is pre-define module aahe & it have passw1, passw2, username like properties """


class NewUserForm(UserCreationForm):            # UserCreationForm form se auth-user wale form mai entry jayegi
    # js name database(auth-user) mdhe aahe tsch ethe ghayche otherwise error yenar
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)  
    email = forms.EmailField(required=True)     # required=True means email field compulsory hai


    class Meta:
        model = User 
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):                                  # Hum ye method overriding kr rhe hai UserCreationForm se
        user = super(NewUserForm, self).save(commit=False)        # commit=False hai means obj create hoga bt vo database mai save nhi hoga
        print(user.__dict__)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        # user.is_staff = True                 # In order to get the access for admin UI (user ka is_staff status 1 show hoga)

        if commit:                          # When this commit is True then data(i.e object) will get save in database 
            user.save()                     # & here we using functions commit [ie. def save(self, commit=True):]
        return user                         # yaha user-obj return hoga & then views.py mai use kiya (ie.  user = form.save())