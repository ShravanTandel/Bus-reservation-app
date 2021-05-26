from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from . models import Company, BusInfo, Passenger, Seats, Rating

class SeatForm(forms.ModelForm):
    seatno = forms.CharField(max_length = 20,label="Seat No",widget=forms.TextInput(attrs={'class':'form-control col-xs-4','placeholder': 'Seat No','required':'true'}))
    class Meta():
        model = Seats
        fields = ('seatno',)

class PassengerForm(forms.ModelForm):
    name = forms.CharField(max_length = 20,label="Name",widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    age = forms.CharField(max_length = 20,label="Age",widget=forms.TextInput(attrs={'placeholder': 'Age'}))
    emailid = forms.CharField(max_length = 20,label="Email Id",widget=forms.TextInput(attrs={'placeholder': 'Email Id'}))
    phoneno = forms.CharField(max_length = 20,label="Phone No",widget=forms.TextInput(attrs={'placeholder': 'Phone No'}))
    
    class Meta():
        model = Passenger
        fields = ('name','gender','age','emailid','phoneno',)
        widgets = {
            'name': forms.TextInput(attrs = {'class':'form-control','required':'true'}),
            'age': forms.TextInput(attrs = {'class':'form-control','required':'true'}),
            'emailid': forms.TextInput(attrs = {'class':'form-control','required':'true'}),
            'phoneno': forms.TextInput(attrs = {'class':'form-control','required':'true'}),
        }


class UserForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'required':'true'}))
    username = forms.CharField(max_length = 20,label="Username",widget=forms.TextInput(attrs={'placeholder': 'Username','required':'true'}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'placeholder': 'Email','required':'true'}))
    class Meta():
        model = User
        fields = ('username','email','password',)
        widgets = {
            'username': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Username'}),
            'email': forms.EmailInput(attrs = {'class':'form-control', 'placeholder':'Email'}),
            'password': forms.PasswordInput(attrs = {'class':'form-control', 'placeholder':'Password'}),
        }

class Busform(forms.ModelForm):
    class Meta():
        model = BusInfo
        fields = ('busno','company','source','destination','departuretime','date','bustype','duration','price',)
        widgets = {
            'busno': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Bus No','required':'true'}),
            'company': forms.Select(attrs = {'class':'form-control','required':'true'}),
            'source': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Source','required':'true'}),
            'destination': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Destination', 'required':'true'}),
            'departuretime': forms.TimeInput(attrs = {'class':'form-control', 'placeholder':'Departure Time','required':'true'}),
            'date': forms.DateInput(attrs = {'class':'form-control','type':'date','required':'true'}),
            #'bustype': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Bus Type (AC / NON AC)','required':'true'}),
            'duration': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Duration','required':'true'}),
            'price': forms.NumberInput(attrs = {'class':'form-control', 'placeholder':'Price','required':'true'}),
        }

class Companyform(forms.ModelForm):
    name = forms.CharField(max_length = 20,label="Company Name",widget=forms.TextInput(attrs={'placeholder': 'Company Name','required':'true'}))

    class Meta():
        model = Company
        fields = {'name',}
        widgets = {
                'name': forms.TextInput(attrs = {'class':'form-control'}),
        }

class RatingForm(forms.ModelForm):

    class Meta():
        model = Rating
        fields = {'rate', 'experience'}

        widgets = {
            'experience': forms.TextInput(attrs = {'class':'form-control'})
        }
        
