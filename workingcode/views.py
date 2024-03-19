from django.shortcuts import render
from .models import formdata
# from .models import photomodel

# Create your views here.
def home(request):
    if request.method == 'POST':
        nfirstname = request.POST['firstname']
        nlastname = request.POST['lastname']
        nemail = request.POST['email']
        nphone = request.POST['phone']

        new_inputtext = formdata(firstname=nfirstname, lastname=nlastname, email=nemail, phone=nphone)
        new_inputtext.save()


    # if request.method == 'POST':
    #     nphoto = request.POST['photo']

    #     new_photo = photomodel(phone=nphone)
    #     new_photo.save()






    return render(request, 'home.html')

def project(request):
    return render(request, 'project.html')
