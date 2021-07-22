from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def eleShow(request):
    strMessage = '<body style="background-color:#a3ccae"><h1>Electronics : </h1><br><ol><li><a href="items/computer" style="text-decoration:none"><h3> Computer & Accessorties</h3></a></li><br><li><a href="items/homeappliances" style="text-decoration:none"><h3> Home Apliances</a></h3></li></body>'
    return HttpResponse(strMessage)

def compShow(request):
    strMessage = '<body style="background-color:#a3ccae"><br><h3>This is redirected page for computer</h3></body>'
    return HttpResponse(strMessage)

def homeAppliancesDetails(request):
    strMessage = '<body style="background-color:#a3ccae"><br><h3>This is redirected page for Home-Apliances</h3></body>'
    return HttpResponse(strMessage)