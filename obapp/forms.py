from django import forms
from .models import Restaurant,Employee



class RestForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = [
            'name',
            'res_type',
            'address'
        ]


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = [
            'name',
            'salary',
            'email',
            'mobile'
        ]
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if len(mobile) > 10:
            raise forms.ValidationError("invalid mobile number")
        if not mobile.isdigit():
            raise forms.ValidationError("mobile must contains only the digits only.")
        



