from django.shortcuts import render

# Create your views here.
def accDetails(request):
    accDict = {"AccountId":8497613894837,"AccHolder":"Mr. XYZ", "Balance":1303890}
    return render(request,'bankDetails.html',accDict)