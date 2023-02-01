from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.
def django_form(request):
    formobject=Studentsform()
    d={'form':formobject}

    if request.method=='POST':
        FormData=Studentsform(request.POST)
        #return HttpResponse(FormData)

        if FormData.is_valid():           # Validation
            n=FormData.cleaned_data['name']           # dict_name[key] = value   class attribute variables are keys
            a=FormData.cleaned_data['age']
            e=FormData.cleaned_data['email']  # Process

            d1={'n':n, 'a':a, 'e':e}
            return render(request, 'Form_data.html',d1)  # collected data returning as html page

    return render(request, 'django_form.html',d)