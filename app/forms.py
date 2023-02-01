from django import forms

g=[('male','M'), ('female','F')]
c=[('python','Python'),('django','django'),('sql','sql'),('webtech','webtech')]
m=[('AWS','AWS'),('Aptitude','Aptitude')]

class Studentsform(forms.Form):  # 1 form
    name=forms.CharField(max_length=100) # 1 input tag
    age=forms.IntegerField(min_value=5)
    email=forms.EmailField(max_length=90)
    passward=forms.CharField(min_length=8,max_length=20,widget=forms.PasswordInput)
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g, widget=forms.RadioSelect)
    course=forms.MultipleChoiceField(choices=c)
    additonal=forms.MultipleChoiceField(choices=m, widget=forms.CheckboxSelectMultiple)
    address=forms.CharField(max_length=1000, widget=forms.Textarea)
