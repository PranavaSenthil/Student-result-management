from django import forms

from .models import year,subject,student,result

class yearform(forms.ModelForm):

    class Meta:
        model = year
        fields = '__all__'

class subjectform(forms.ModelForm):

    class Meta:
        model = subject
        fields = '__all__'

class studentform(forms.ModelForm):
     
   class Meta:
        model = student
        fields = '__all__'

class resultform(forms.ModelForm):
    
    class Meta:
        model = result
        fields = ('Sno','student_ID','name','semester','subjects','grade','status')