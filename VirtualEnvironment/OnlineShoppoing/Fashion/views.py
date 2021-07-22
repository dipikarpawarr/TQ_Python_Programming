from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fashionData(request):
    strMessage = '<body style="background-color:#a3ccae"><h1>Fashion : </h1><br><ol><li><a href="items/cloths" style="text-decoration:none"><h3> Cloths</h3></a></li><br><li><a href="items/footwear" style="text-decoration:none"><h3> Footwear</a></h3></li><br><li><a href="items/cosmatics" style="text-decoration:none"><h3> Cosmatics</a></h3></li></body>'
    return HttpResponse(strMessage)

def clothsDetails(request):
    strMessage = '<body style="background-color:#a3ccae"><br><h3>You Are On Cloths Section</h3><br><br><h3>* Ethnic Wear<br>* Party Wear<br></h3></body>'
    return HttpResponse(strMessage)

def footwearDetails(request):
    strMessage = '<body style="background-color:#a3ccae"><br><h3>You Are On Foot-Wear Section</h3><br><br><h3>* Sports<br>* Daily<br>* Rainy<br>* Summer</h3></body>'
    return HttpResponse(strMessage)

def consmaticDetails(request):
    strMessage = '<body style="background-color:#a3ccae"><br><h3>You Are On Cosmatics Section</h3><br><br><h3>* Skin Care<br>* Hair Care<br></h3></body>'
    return HttpResponse(strMessage)