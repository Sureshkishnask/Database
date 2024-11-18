from django.shortcuts import render
from .models import Datas
# Create your views here.
def home(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        email=request.POST['mail']
        obj=Datas()
        obj.Name=name
        obj.Age=age
        obj.Address=address
        obj.Contact=contact
        obj.Email=email
        obj.save()
    return render(request,"home.html")
