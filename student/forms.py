from django import forms

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['rollno', 'dob']
 