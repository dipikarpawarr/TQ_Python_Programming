from Library.models import *
from django import forms

class Sign_Up_Form(forms.ModelForm):
    class Meta:
        model = SignUp_Model
        fields = '__all__'

class Login_Form(forms.ModelForm):
    class Meta:
        model = Login_Model
        fields = '__all__'

class Add_Book_Form(forms.ModelForm):
    class Meta:
        model = Books_Model
        fields = '__all__'

class Issue_Book_Form(forms.ModelForm):
    class Meta:
        model = Issue_Book_Model
        fields = '__all__'

class Return_Book_Form(forms.ModelForm):
    class Meta:
        model = Return_Book_Model
        fields = '__all__'

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Books_Model
        fields = '__all__'

class DeleteForm(forms.ModelForm):
    class Meta:
        model = Books_Model
        fields = '__all__'
